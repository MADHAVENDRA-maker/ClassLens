import dlib
import numpy as np
import face_recognition_models
import streamlit as st
from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )
    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    return detector,sp,facerec
def get_face_embeddings(image_np):
    detector,sp,facerec = load_dlib_models()
    faces = detector(image_np,1)
    encoding = []
    for face in faces:
        shape = sp(image_np,face)
        face_descriptor = facerec.compute_face_descriptor(image_np,shape,1)
        encoding.append(np.array(face_descriptor))
    return encoding
@st.cache_resource
def get_trained_model():
    x = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get("face_embedding")
        if embedding:
            x.append(np.array(embedding))
            y.append(student.get("student_id"))

    if len(x) == 0:
        return None

    return {
        "x": x,
        "y": y
    }
def train_model():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)
def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_students = {}

    model_data = get_trained_model()
    if not model_data:
        return {}, [], 0

    x_train = model_data["x"]
    y_train = model_data["y"]

    all_students = sorted(list(set(y_train)))

    resemblance_threshold = 0.7

    for encoding in encodings:
        best_distance = float("inf")
        best_student = None

        for stored_embedding, student_id in zip(x_train, y_train):
            distance = np.linalg.norm(stored_embedding - encoding)

            if distance < best_distance:
                best_distance = distance
                best_student = student_id

        if best_distance <= resemblance_threshold:
            detected_students[int(best_student)] = True

    return detected_students, all_students, len(encodings)
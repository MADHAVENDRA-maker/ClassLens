import streamlit as st
from src.ui.base_layout import style_base_dashboard
from src.ui.base_layout import style_base_layout
from src.components.header import header_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance
from src.database.db import get_all_students
from src.pipelines.face_pipeline import get_face_embeddings
from src.pipelines.voice_pipeline import get_voice_embeddings
from src.pipelines.face_pipeline import train_model
from src.database.db import create_student
from src.components.enroll_dialog import enroll_dialog
from src.database.db import get_student_subjects
from src.database.db import get_student_attendance
from src.components.subject_card import subject_card
from src.database.db import unenroll_student_to_subject

def student_dashboard():
    student_data = st.session_state.student_data
    c1,c2 = st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {student_data['name']}""")
        if st.button("Logout",type="secondary",key="loginbackbtn",shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()
    st.space()
    c1,c2 = st.columns(2)
    with c1:
        st.header("Your enrolled subjects")
    with c2:
        if st.button("Enroll in subject",type="primary",width="stretch"):
            enroll_dialog()
    st.divider()
    with st.spinner("Loading your enrolled subjects.."):
        subjects = get_student_subjects(student_data["student_id"])
        logs = get_student_attendance(student_data["student_id"])
    stats_map = {}
    for log in logs:
        sid = log["subject_id"]
        if sid not in stats_map:
            stats_map[sid] = {"total":0,"attended":0}
        stats_map[sid]["total"] = stats_map[sid]["total"] + 1
        if log.get("is_present"):
            stats_map[sid]["attended"] = stats_map[sid]["attended"] + 1
    cols = st.columns(2)
    for i,sub_node in enumerate(subjects):
        sub = sub_node["subjects"]
        sid = sub["subject_id"]
        stats = stats_map.get(sid,{"total":0,"attended":0})
        def unenroll_btn():
            if st.button("Unenroll from this course",type="tertiary",width="stretch"):
                unenroll_student_to_subject(student_data["student_id"],sid)
                st.toast(f'Unenrolled from {sub["name"]} successfully!')
                st.rerun()
        with cols[i%2]:
            subject_card(
                name=sub["name"],
                code=sub["subject_code"],
                section=sub["section"],
                stats=[("Total",stats["total"]),
                       ("Attended",stats["attended"])],
                footer_callback=unenroll_btn()
            )




def student_screen():
    style_base_dashboard()
    style_base_layout()
    if "student_data" in st.session_state:
        student_dashboard()
        return
    c1,c2 = st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home",type="secondary",key="loginbackbtn",shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
    st.header("Login using Face ID",text_alignment="center")
    st.write("Choose how you would like to upload your image")
    st.space()
    st.space()
    show_registration = False
    photo_source = st.camera_input("Postion your face in the center")
    if photo_source:
        img = np.array(Image.open(photo_source).convert("RGB"))
        with st.spinner("AI is scanning.."):
            detected,all_ids,num_faces = predict_attendance(img)
            if num_faces==0:
                st.warning("Face not found")
            elif num_faces>1:
                st.warning("Multiple faces found")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s["student_id"]==student_id),None)
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = "student"
                        st.session_state.student_data = student
                        st.toast(f"Welcome back, {student['name']}")
                        st.rerun()
                else:
                    st.info("Face not recognized, you might be a new student")
                    show_registration = True
    if show_registration:
        with st.container(border=True):
            st.header("Register new profile")
            new_name = st.text_input("Enter your name")
            st.subheader("Optional: Voice Enrollment")
            st.info("Enroll for voice only attendance")
            audio_data = None
            try:
                audio_data = st.audio_input("Record a short phrase which include sentences like \"I am present\" and \"My name is ..\"")
            except Exception:
                st.error("Audio data failed")
            if st.button("Create Account",type="primary"):
                if new_name:
                    with st.spinner("Creating profile.."):
                        img = np.array(Image.open(photo_source).convert("RGB"))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_embeddings = encodings[0].tolist()
                            voice_embeddings = None
                            if audio_data:
                                voice_embeddings = get_voice_embeddings(audio_data.read())
                            response_data = create_student(new_name,face_embedding=face_embeddings,voice_embedding=voice_embeddings)
                            if response_data:
                                train_model()
                                st.session_state.is_logged_in = True
                            st.session_state.user_role = "Student"
                            st.session_state.student_data = response_data[0]
                            st.toast(f"Profile created! Hi {new_name}")
                            st.rerun()
                        else:
                            st.error("Couldn't capture your facial features for registraion")
                else:
                    st.warning("Please enter your name")
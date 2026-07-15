import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject




@st.dialog("Enroll in subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher to enroll")
    join_code = st.text_input("Subject Code")
    if st.button("Enroll now!",type="primary",width="stretch"):
        if join_code:
            response = supabase.table("subjects").select("subject_id","name","subject_code").eq("subject_code",join_code).execute()
            if response.data:
                subject = response.data[0]
                student_id = st.session_state.student_data["student_id"]
                check = supabase.table("subject_students").select("*").eq("subject_id",subject["subject_id"]).eq("student_id",student_id).execute()
                if check.data:
                    st.warning("You are already renrolled in this program")
                else:
                    enroll_student_to_subject(student_id,subject["subject_id"])
                    st.success("Successfully enrolled")
                    st.rerun()
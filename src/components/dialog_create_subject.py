import streamlit as st
from src.database.db import create_subject



@st.dialog("Create new subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the detials of the new subject")
    sub_code = st.text_input("Subject code")
    sub_name = st.text_input("Subject name")
    sub_section = st.text_input("Section")
    if st.button("Create subject now",type="primary",width="stretch"):
        if sub_name and sub_code and sub_section:
            try:
                create_subject(sub_code,sub_name,sub_section,teacher_id)
                st.toast("Subject created successfully")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")
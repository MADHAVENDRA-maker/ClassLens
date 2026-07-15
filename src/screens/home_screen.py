import streamlit as st
from src.ui.base_layout import style_base_home
from src.ui.base_layout import style_base_layout
from src.components.header import header_home
from pathlib import Path


def home_screen():
    header_home()
    style_base_home()
    style_base_layout()
    col1,col2 = st.columns(2,gap="large")
    with col1:
        st.header("I am a student")
        student_path = Path(__file__).parent /"student_image.png"
        st.image(str(student_path),width=150)
        if st.button('Student Portal',type="primary",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state['login_type'] = 'student'
            st.rerun()
    with col2:
        st.header("I am a teacher")
        teacher_path = Path(__file__).parent /"teacher_image.png"
        st.image(str(teacher_path),width=150)
        if st.button('Teacher Portal',type="primary",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state['login_type'] = 'teacher'
            st.session_state.teacher_login_type = 'login'
            st.rerun()
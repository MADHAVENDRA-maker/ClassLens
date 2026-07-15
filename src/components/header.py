import streamlit as st
from pathlib import Path
import base64




def header_home():
    logo_path = Path(__file__).parent /"home_page_logo.png"
    with open(logo_path,"rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px">
            <img src="data:image/png;base64,{encoded_image}" style='height:100px;'/>
            <h1 style='text-align:center; color: black'>ClassLens</h1>
                """
            ,unsafe_allow_html=True)
def header_dashboard():
    logo_path = Path(__file__).parent /"home_page_logo.png"
    with open(logo_path,"rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap: 10px;">
            <img src="data:image/png;base64,{encoded_image}" style='height:85px;'/>
            <h2 style='text-align:left; color:#5865F2'>ClassLens</h2>
                """
            ,unsafe_allow_html=True)
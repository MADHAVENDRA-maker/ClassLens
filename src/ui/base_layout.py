import streamlit as st




def style_base_home():
    st.markdown("""
        <style>
                .stApp {
                    background: #F1F5F9 !important;
                }

                .stApp div[data-testid="stColumn"]{
                background: white !important;
                padding: 2.5rem !important;
                border-radius: 2rem !important;
                border: 1px solid #334155 !important!;
                box-shadow: 0 4px 12px rgba(15,23,42,0.06);
                }
        </style>
                """
            ,unsafe_allow_html=True)
def style_base_dashboard():
    st.markdown("""
        <style>
                .stApp {
                background: #F1F5F9 !important;
                }
        </style>
                """
            ,unsafe_allow_html=True)
def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Inter:wght@300;400;500;600;700;800&display=swap');
                
                #MainMenu, footer, header {
                visibility: hidden;
                }

                .block-container {
                padding-top:1.5rem !important
                }

                h1 {
                font-family: 'Space Grotesk',sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.05 !important;
                margin-bottom: 0rem !important;
                font-weight: 700 !important;
                }

                h2 {
                font-family: 'Space Grotesk',sans-serif !important;
                font-size: 1.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                font-weight: 700 !important;
                }
                
                button[kind="secondary"]{
                border-radius: 14px !important;
                background-color: #E2E8F0 !important;
                color: #0F172A !important;
                border: 1px solid #CBD5E1 !important;
                transition: transform 0.25s ease-in-out !important;
                font-family: 'Inter',sans-serif !important;
                font-weight: 600 !important;
                }

                button[kind="primary"]{
                border-radius: 14px !important;
                background: #2563EB !important;
                color: white !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                font-family: 'Inter',sans-serif !important;
                font-weight: 600 !important;
                }

                button[kind="tertiary"]{
                border-radius: 14px !important;
                background: white !important;
                color: #334155 !important;
                border: 1px solid #CBD5E1 !important;
                transition: transform 0.25s ease-in-out !important;
                font-family: "Inter",sans-serif !important;
                font-weight: 600 !important;
                }

                button:hover {
                transform: translateY(-2px);
                filter: brightness(1.08);
                }
                
        </style>
                """
            ,unsafe_allow_html=True)
import streamlit as st
from home import home

# Cấu hình chung cho trang
st.set_page_config(
    page_title="Dog & Cat Classifier",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed",
    
)

home()

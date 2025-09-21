import streamlit as st
from home import home

# Configure page settings
st.set_page_config(
    page_title="Dog & Cat Classifier",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed",
    
)

# Launch home page UI
home()

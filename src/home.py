import streamlit as st
import os
from task import predict_img

# Home page
def home():
    st.markdown("<h1 style='text-align: center; font-size: 68px'>🐶🐱 Dog & Cat Image Classification 😺🐶</h1>", unsafe_allow_html=True)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Căn giữa ảnh
    #col1, col2, col3 = st.columns([1, 2, 1]) 
    #with col2:
        #IMAGE_PATH = os.path.join(BASE_DIR, "..", "assets", "picture.jpg")
        #st.image(IMAGE_PATH, width=650)  # Resize ảnh + căn giữa

    st.write("### 👇 Just a click to upload an image and find out if it's a dog or a cat! ✨")
    img = st.file_uploader("📂 Choose an image...", type=["jpg", "jpeg", "png"])

    if img is not None:
        col1, col2, col3 = st.columns([1, 2, 1]) 
        with col2:
            st.image(img, caption="Uploaded Image", width=700)
            with st.spinner("🔄 Predicting... Please wait!"):
                class_name, confidence = predict_img(img)
        st.success(f"🎯 Prediction: **{class_name}** ({confidence:.2%})")

    st.divider()
    st.write("#### 👩‍💻 Developed by: Lê Nguyễn Thiên An")
    st.write("#### ✉️ Contact: lenguyenthienan2004@gmail.com")

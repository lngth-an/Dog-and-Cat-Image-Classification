import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model 

# Load model và labels
def load_model_and_labels():
    model = load_model("model/keras_model.h5", compile=False)
    
    labels = {}
    with open("model/labels.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue 
            class_id = int(line[0])
            class_name = line[2:]
            labels[class_id] = class_name
    
    return model, labels

def preprocess_img(img, target_size=(224, 224)):
    img = load_img(img, target_size=target_size)
    img_array = img_to_array(img) / 225.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_img(img):
    if img is None:
        return None, None 
    
    model, labels = load_model_and_labels()
    img_array = preprocess_img(img)
    
    result = model.predict(img_array)
    class_id = int(np.argmax(result))
    class_name = labels[class_id]
    confidence = float(np.max(result))
    
    return class_name, confidence
import os
import streamlit as st
import numpy as np
import pytesseract
from PIL import Image

# Installing Tesseract and language data (only if needed)
if not os.path.isfile('/usr/bin/tesseract'):
    st.warning('Installing Tesseract...')
    os.system('apt-get update')
    os.system('apt-get install -y tesseract-ocr')
    os.system('apt-get install -y tesseract-ocr-hin')

# Specify the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

st.title("Our OCR APP")
st.text("Upload an image which contains English or Hindi Text")

# Upload the image
upload_image = st.sidebar.file_uploader('Choose an image input for conversion', type=["jpg", "png", "jpeg"])

if upload_image is not None:
    # Open the uploaded image
    img = Image.open(upload_image)
    
    # Display the image
    st.image(upload_image)
    
    # Extract text when the button is clicked
    if st.button("Extract Text"):
        st.write("Extracted Text")
        
        # Extract text in both Hindi and English languages
        output_text = pytesseract.image_to_string(img, lang='eng+hin')
        
        # Display the extracted text
        st.write(output_text)

from dotenv import load_dotenv
load_dotenv() # load all environment functions

import streamlit as st # type: ignore
import os
import google.generativeai as genai # type: ignore
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Load the gemini models
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input !="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text
#setting up Stremlit
st.set_page_config(page_title="Gemini Image Demo")
st.header("LLM Gemini models working")
input = st.text_input("Input Image:", key="Input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Check if a file has been uploaded

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit=st.button("Tell Me About the Image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is:")
    st.write(response)
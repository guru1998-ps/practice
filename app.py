from dotenv import load_dotenv
load_dotenv() #load all enviroment  variables

import streamlit as st # type: ignore
import os
import google.generativeai as genai # type: ignore

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini pro and get response

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text
#setting up streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM application")
input = st.text_input("Input:", key="Input")
submit=st.button("Ask the Question")
# when submit is clicked
if submit:

    response = get_gemini_response(input)
    st.subheader("the response is :")
    st.write(response)


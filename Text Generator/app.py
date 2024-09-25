import google.generativeai as genai
from dotenv import load_dotenv
import os 
import streamlit as st

load_dotenv()
sec_key = os.getenv('google_api_key')


genai.configure(api_key = sec_key)



st.title("Text Generation")


input = st.text_area("Enter your prompt here")


submit = st.button("Generate Text")

model = genai.GenerativeModel('gemini-1.5-flash')

if submit:

    response = model.generate_content(input)

    st.header("Here is the response:")

    st.write(response.text)
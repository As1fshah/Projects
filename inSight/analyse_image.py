import streamlit as st
import google.generativeai as genai 
import os
from dotenv import load_dotenv
from PIL import Image
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser    

# Import Ends here

# --- Pre-requisites starts from here ---

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if google_api_key is not None:
    genai.configure(api_key=google_api_key)

else:
    st.write("Invalid API Key")

model = genai.GenerativeModel('gemini-1.5-flash')

parser = JsonOutputParser()



# prompt = """
# You are an Expert Image anlayst working on a clients project, your client will provide you a set of image.
# from those image/ images, you have to extrct the information.
# and generate the response in the following format:

# 'information': Answer what this image is all about ? around 30-50 words.
# 'person' : if you can identify the person and if the person is famous personality print the name around 10-30 words.
# 'objects': name all of the object you have found in a image.
# 'summary' : generate a quick summary about the recieved image around 50 words.

# return the json object of the same with the above information.
# """

def extract_info(img):
        prompt = """
        You are an Expert Image anlayst working on a clients project, your client will provide you a set of image.
        from those image/ images, you have to extrct the information.
        and generate the response in the following format:

        'information': Answer what this image is all about ? around 30-50 words.
        'person' : if you can identify the person and if the person is famous personality print the name around 10-30 words.
        'objects': name all of the object you have found in a image.
        'summary' : generate a quick summary about the recieved image around 50 words.

        return the json object of the same with the above information.
        """

        if prompt !="": # if we have any prompts
            model_response = model.generate_content([img, prompt])
            response = model_response.text

        else: # if we dont have any prompts 

            model_response = model.generate_content(img)
            response = model_response.text

        output = parser.parse(response)

        return output
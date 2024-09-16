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


st.title("Information Retrieval with Image")

st.write("Upload an image and get the text from the image")

    # --- Pre-requisites ends here ---


    # From here your actual image processing code starts


uploaded_file = st.file_uploader("Upload your image here", type = ['jpg', 'jpeg', 'png'])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # st.image(image, caption = 'Uploaded Image', use_column_width = True)


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

def analyse_image(img, prompt):
        if prompt !="": # if we have any prompts
            model_response = model.generate_content([image, prompt])
            response = model_response.text

        else: # if we dont have any prompts 

            model_response = model.generate_content(image)
            response = model_response.text

        output = parser.parse(response)

        return output

submit = st.button('Generate Text')

if submit:
        with st.spinner('Analysing Image...'):

            output = analyse_image(image, prompt)

            st.success('Processing Complete')

            st.image(image, caption = "Here is the Uploaded Image", use_column_width=True)
            
            col_1, col_2 = st.columns(2)
            col_3, col_4 = st.columns(2)
            with col_1:
                with st.expander("Quick information about the uploaded image: "):
                    st.write(output['information'])
            with col_2:
                with st.expander("We've found this person: "):
                    st.write(output['person'])
            with col_3:
                with st.expander("Objects we've found in this image: "):
                    st.write(output['objects'])
            with col_4:
                with st.expander("Summary: "):
                    st.write(output['summary'])
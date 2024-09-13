import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain.chains import LLMChain

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

# Set up the LLM
llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash', 
                             api_key=google_api_key, 
                             temperature= 0)


def input_name_verification(name):
    celeb_name = name
    
    name_ver_template = f"""

    Given the name of a celebrity, can you verify if the name is correct? and known as famous personality, Please answer with a simple yes or no.

    Name: {celeb_name}.


    """
    name_ver_prompt = PromptTemplate(template = name_ver_template)

    name_ver_prompt_chain_2 = LLMChain(llm = llm, prompt = name_ver_prompt, output_key = 'name_verification')


    name_ver_prompt_response = name_ver_prompt.invoke({"name":celeb_name})

    return name_ver_prompt_response

    

def generate_response(name):

    celeb_name = name


    initial_prompt_2 = f"""

    write an one or two liner very famous quote from {celeb_name} and highlight his/her name.
    within 50 words
    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones

    """


    prompt_2 = PromptTemplate(template = initial_prompt_2)

    chain_2 = LLMChain(llm = llm, prompt = prompt_2, output_key = 'achievements')


    response = chain_2.invoke({"name":celeb_name})

    return response

def display_reponse(obj):
    content = st.write(obj['achievements'])

    return content

 



input = st.text_input( placeholder="Enter you Prompt Here", label = '')
search = st.button('Search')





if search:
    with st.spinner('In Progress...'):

        name_ver_prompt_response = generate_response(input)
        
        st.success('Processing Complete')
        display_reponse(name_ver_prompt_response)

    
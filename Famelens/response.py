from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", 
                       temperature= 0,
                       api_key= google_api_key)


def get_response(name):

    celeb_name = name

    initial_prompt_1 = f"""You are a celebrity expert. You are given a name of a celebrity.
    celebrity name is : {celeb_name}.
    Write a short bio about him / her.
    remember to keep the lenght of this short bio must not exceed more than 150 words and 2 paragraphs max,

    and if required we may ask you more details about the celebrity, if so, do answer the asked questions. """


    prompt_1 = PromptTemplate(template = initial_prompt_1)

    chain_1 = LLMChain(llm = llm, prompt = prompt_1, output_key = 'introduction')

    initial_prompt_2 = f"""

    what are top 5 key achievements of {celeb_name} so far in his/her career, 
    and give me the details of each achievement in a sequence format.
    try to keep the response in a one liner for each achievement.
    don't add any other information apart from achievements of the celebrity.
    only highlight the achievement from statement in bold letters and keep the rest of the information in normal letters.
    also add the source of the information  of the achievement statement in this format: "(Source: <source>)" in next line.
    for example: id this is an achievement of {celeb_name}: "Winning 14 Filmfare Awards, making him the most awarded actor in the ceremony's history.
    " Highlight the keyword which represent event or thing he has done, here you should highlight "Filmfare Awards" in bold letters.
    
    generate the response without any introductory part, instead add "These are top 5 achievements of {celeb_name} so far in his/her career. " at the start of the response. 
    
    add short summary of all achievemets statement about one or two lines then proceed to achievments.

    conclude the response with a quote that this information is best of my knowledge in best possible manner.

    Note: Don't provide any of the wrong information do verify the information about the achievements, if you are not sure on this go for some other availble and verified ones.

    """


    prompt_2 = PromptTemplate(template = initial_prompt_2)

    chain_2 = LLMChain(llm = llm, prompt = prompt_2, output_key = 'achievements')


    initial_prompt_3 = f"""

    Can you please mention the full name of {celeb_name} below mentioned peoples in here

    1. Father's Name: abc
    2. Mother's Name:
    3. Spouse's Name:
    4. Childrens: if they do
    5. Family Origin:


    start the response with statement something like "Family of {celeb_name} is as follows:"
    write a short summary about his/her family to then proceed to fetch names.

    conclude the response with a quote that this information is best of my knowledge in best possible manner.


    """


    prompt_3 = PromptTemplate(template = initial_prompt_3)

    chain_3 = LLMChain(llm = llm, prompt = prompt_3, output_key = 'family_background')


    initial_prompt_4 = f"""

    Give me quick brief about the work portfloio of {celeb_name} 

    Keep the content lenght upto 200 words and 2 paragraphs, highlighting the career glimpse of him/her.
    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones.
    Do add a quote that this information is best of my knowledge.


    """


    prompt_4 = PromptTemplate(template = initial_prompt_4)

    chain_4 = LLMChain(llm = llm, prompt = prompt_4, output_key = 'work_portfolio')


    initial_prompt_5 = f"""

    can you mention the top 3 major colaborations of {celeb_name} so far in his/her career if the information available in public. 
    
    create 3 paragraph for each of them with short brief about the colaboration deal with max limit upto 30 words for each.    
    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones.
    Do add a quote that this information is best of my knowledge.

    """


    prompt_5 = PromptTemplate(template = initial_prompt_5)

    chain_5 = LLMChain(llm = llm, prompt = prompt_5, output_key = 'major_colab')


    initial_prompt_6 = f"""

    According to you is {celeb_name} popular on social media platforms, if yes do mention the number of followers on each of the platforms with accuracy.
    
    also if possible do write a short brief about the fee-range they charge in usd for a single post on each of the platforms, if amount goes beyond 4 figures add k or m with amount like 10k or 1M .
    

    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones.
    Do add a quote that this information is best of my knowledge.


    """


    prompt_6 = PromptTemplate(template = initial_prompt_6)

    chain_6 = LLMChain(llm = llm, prompt = prompt_6, output_key = 'social_media')


    initial_prompt_7 = f"""

    also write a short summary about timeline of his career journey within.

    can you mention the timeline career journey of {celeb_name} with use of years specifically and conclude everything within 100 words. :
    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones.
    Do add a quote that this information is best of my knowledge.


    """


    prompt_7 = PromptTemplate(template = initial_prompt_7)

    chain_7 = LLMChain(llm = llm, prompt = prompt_7, output_key = 'growth_analysis')


    initial_prompt_8 = f"""

    Factors contributing to {celeb_name}'s net worth growth within 100 words:
    also write a short summary of the networth increased through out the years.
    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones.
    Do add a quote that this information is best of my knowledge.

    """


    prompt_8 = PromptTemplate(template = initial_prompt_8)

    chain_8 = LLMChain(llm = llm, prompt = prompt_8, output_key = 'net_worth')


    initial_prompt_9 = f"""

    List top 5 investments {celeb_name} so far in thier career except thier profession, and which are known investments in public within 150 words.
    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones.
    Do add a quote that this information is best of my knowledge.


    """


    prompt_9 = PromptTemplate(template = initial_prompt_9)

    chain_9 = LLMChain(llm = llm, prompt = prompt_9, output_key = 'expensive_things')


    initial_prompt_10 = f"""

    List top 5 most notable awards won by {celeb_name} with thier value not in amount, in thier respective domains/field/professions.
    also list top 5 endorsements of {celeb_name} with thier respective brands.
    within 150 words.    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones.
    Do add a quote that this information is best of my knowledge.


    """


    prompt_10 = PromptTemplate(template = initial_prompt_10)

    chain_10 = LLMChain(llm = llm, prompt = prompt_10, output_key = 'awards_endorsements')


    initial_prompt_11 = f"""

    fetch 3 most discussed news about the contraversies / scandals of {celeb_name} through out his/her career so far has received significant attention.
    within 100 words
    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones.
    Do add a quote that this information is best of my knowledge.


    """


    prompt_11 = PromptTemplate(template = initial_prompt_11)

    chain_11 = LLMChain(llm = llm, prompt = prompt_11, output_key = 'contraversies_scandals')



    initial_prompt_12 = f"""

    write an one or two liner very famous quote from {celeb_name} and highlight his/her name.
    within 50 words
    
    Note: Don't provide any of the wrong information do verify the information about these, if you are not sure on this go for some other availble and verified ones

    """


    prompt_12 = PromptTemplate(template = initial_prompt_12)

    chain_12 = LLMChain(llm = llm, prompt = prompt_12, output_key = 'did_you_know')




    main_chain = SequentialChain(chains = [chain_1, chain_2,chain_3, chain_4, chain_5, chain_6, chain_7, chain_8,chain_9,chain_10,chain_11,chain_12],
                    input_variables = ['name'],
                    output_variables = ['introduction', 'achievements','family_background','work_portfolio',
                                        'major_colab', 'social_media','growth_analysis','net_worth',
                                        'expensive_things','awards_endorsements','contraversies_scandals','did_you_know'])
    
    response = main_chain.invoke({"name": celeb_name})
    

    return response




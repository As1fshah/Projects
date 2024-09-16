import streamlit as st
from PIL import Image
from analyse_image import extract_info
from display import display_response


if 'show_intro' not in st.session_state:
    st.session_state.show_intro = True

if st.session_state.show_intro:
    st.title("InSightAI")
    st.header("Discover Meaning in Every Frame")

    title_col_1, title_col_2 = st.columns(2)
    with title_col_1:
        st.image('inSightAI_logo.webp')
    with title_col_2:
        st.subheader("Reveal the Details Behind Every Image")
        st.write("""
                InSightAI is a simple yet powerful image analysis tool that provides quick insights into any picture you upload. 
                 Whether it's identifying objects, recognizing famous personalities, or summarizing the image content, InSightAI makes it easy to discover hidden details. 
                 With just a few clicks, you can uncover information that goes beyond the surface, 
                 making it perfect for casual users and professionals alike.
                """)

    sub_1 = st.button("Let's Try This !")

    
    # When search is clicked, update session state to hide the intro
    if sub_1:
        st.session_state.show_intro = False
    
else:
        st.title("Information Retrieval with Image")

        # st.write("Upload an image and get the text from the image")

        # --- Pre-requisites ends here ---


        # From here your actual image processing code starts


        uploaded_file = st.file_uploader("Upload an image",type = ['jpg', 'jpeg', 'png'])

        image = ""
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            # st.image(image, caption = 'Uploaded Image', use_column_width = True)
        
        submit = st.button("Analyse Image")

        if submit:
                
                with st.spinner('Analysing Image...'):
                    output = extract_info(image)
                    st.success('Processing Complete')
                    st.image(image, caption = "Here is the Uploaded Image", use_column_width=True)
                    display_response(output)


            

            

            

    



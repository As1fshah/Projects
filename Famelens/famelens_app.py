import streamlit as st
from display import display_response
from response import get_response


if 'show_intro' not in st.session_state:
    st.session_state.show_intro = True

if st.session_state.show_intro:
    st.title("FameLens")
    st.header("The Central Station for Celebrity Knowledge")

    title_col_1, title_col_2 = st.columns(2)
    with title_col_1:
        st.image('famelens_logo.webp')
    with title_col_2:
        st.subheader("Discover the World of Celebrities with FameLens")
        st.write("""
                FameLens is an AI-powered platform designed to bring you closer to your favorite celebrities.
                With insights, and detailed profiles, it allows you to explore
                the personal and professional lives of stars in an interactive and engaging way. From key achievements
                and net worth to collaborations and contraversials - FameLens has it all., FameLens lets you focus on the stars you love like never before.
                """)

    sub_1 = st.button("Let's Try This !")

    
    # When search is clicked, update session state to hide the intro
    if sub_1:
        st.session_state.show_intro = False
else:
    st.title("FameLens")
    st.header("The Central Station for Celebrity Knowledge")


    helper_input = st.text_input(placeholder="Enter a celebrity name", label='')

    helper_search = st.button("Search")



    if helper_search:

        if helper_input == "":
            st.write("Please provide the Input")

        if helper_input != "":
            with st.spinner('Fetching details...'):

                response = get_response(helper_input)

                st.success("Processing Complete")

                display_response(response)


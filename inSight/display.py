import streamlit as st

def display_response(obj):
    col_1, col_2 = st.columns(2)
    col_3, col_4 = st.columns(2)

    with col_1:
        with st.expander("Quick information about the uploaded image: "):
            st.write(obj['information'])

    with col_2:
        with st.expander("We've found this person: "):
            st.write(obj['person'])

    with col_3:
        with st.expander("Objects we've found in this image: "):
            st.write(obj['objects'])

    with col_4:
        with st.expander("Summary: "):
            st.write(obj['summary'])

import streamlit as st

def display_response(obj):

    st.title("Intoduction")
    st.write(obj['introduction'])


    with st.expander("Key Achievements"):
        st.write(obj['achievements'])

    with st.expander("Family Background"):
        st.write(obj['family_background'])

    with st.expander("Work Portfolio"):
        st.write(obj['work_portfolio'])

    with st.expander("Major Colaborations"):
        st.write(obj['major_colab'])

    with st.expander("Social Media Followings"):
        st.write(obj['social_media'])

    with st.expander("Career Growth Analysis"):
        st.write(obj['growth_analysis'])


    with st.expander("Net worth"):
        st.write(obj['net_worth'])

    with st.expander("Investments & Assets", ):
        st.write(obj['expensive_things'])

    with st.expander("Awards and Endorments"):
        st.write(obj['awards_endorsements'])


    with st.expander("Contraversies & Scandals"):
        st.write(obj['contraversies_scandals'])

    with st.expander("Famous Quote"):
        st.write(obj['did_you_know'])





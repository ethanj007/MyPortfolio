import streamlit as st
st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images (1)/photo.png")
with col2:
    st.title("Ethan Joshua")
    content = '''hi there im ethan and im currently doing my 2nd year at srm.. ive taken btech cse with cyber security
    and im a vivid learner'''
    st.info(content)
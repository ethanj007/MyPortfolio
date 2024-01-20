import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images (1)/photo.png")
with col2:
    st.title("Ethan Joshua")
    content = '''hi there im ethan and im currently doing my 2nd year at srm.. ive taken btech cse with cyber security
    and im a vivid learner'''
    st.info(content)

content2 = '''
Below you can find some of the apps i have built in python. Feel free to contact me!!
'''
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[1:].iterrows():  # seperating into 2 columns

        st.header(row["title"])
        st.write(row["description"])  # normal font
        st.image("images (1)/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows(): #seperating into 2 columns

        st.header(row["title"])
        st.write(row["description"])  # normal font
        st.image("images (1)/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
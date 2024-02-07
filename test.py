import streamlit as st
import pandas
st.set_page_config(layout="wide")

st.header("The Best Company")
st.write('''i walk a lonely road the only road i have been before dont know where it goes 
but its the end and i walk alone my shadow is what ull find me my shadow makes my heart afraid''')

st.subheader("Our Team")

col3 , col4, col5 = st.columns(3)
df = pandas.read_csv("datas.csv", sep=",")
with col3:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}') # header font
        st.write(row["role"])  # normal font
        st.image("images (2)/" + row["image"])

with col4:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}') # header font
        st.write(row["role"])  # normal font
        st.image("images (2)/" + row["image"])
with col5:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}') # header font
        st.write(row["role"])  # normal font
        st.image("images (2)/" + row["image"])




import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images (1)/ETHAN.png")
with col2:
    st.title("Ethan Joshua")
    content = '''I'm Ethan, a 19-year-old second-year Computer Science student specializing in Cyber Security at SRM. 
    Proficient in Java, I've successfully developed projects that highlight my technical abilities. I'm a fast learner, 
    currently immersing myself in Python and actively working on projects to expand my skill set.
    My passion revolves around the synergy of security and coding, reflecting a deep interest in fortifying digital landscapes. I'm dedicated to mastering various programming languages, and my commitment to cybersecurity positions me as a promising professional in the field. With a proven track record of project accomplishments 
    and a forward-thinking approach to learning, I'm excited to make meaningful contributions to the ever-evolving world of computer science and cybersecurity.'''
    st.info(content)

content2 = '''
Below you can find some of the apps i have built in python. Feel free to contact me!!
'''
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():  # seperating into 2 columns

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

import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG", width=500)

with col2:
    st.title('Jakub Kalamaszek')
    content = """
    EN: Hi, I am Jakub Kalamaszek,  I am 2 degree student of Automation control an Metrology. I am looking
    for an internship as a PLC programmer or related to the Automation or IT industry.
    \nPL: Witam, Nazywam się Jakub Kalamaszek jestem studentem 2-stopnia na kierunku Automatyka i Metrologia. Szukam
    stażu związanego z branżą automatyki bądź IT.
    """
    st.info(content)

content2 = """
Below you can find a video presenting my Robot Bartender project made in the CODESYS environment.
"""

content4 = """
Below you can find a video presenting my Stairs Climbing Robot with a one-kilogram payload which I created with my friends.
"""

video_file = open('images/demo.mp4', 'rb')
video_bytes = video_file.read()

col5, empty_col, col6 = st.columns([1.5, 0.5, 1.5])
with col5:
    st.info(content2)
    st.video('https://www.youtube.com/watch?v=RlJ262EYSzw')

with col6:
    st.info(content4)
    st.video(video_bytes)
    st.write(f"[Source Code](https://github.com/Jelon455/stairs-climbing-robot?tab=readme-ov-file)")

content3 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.info(content3)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:9].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[9:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


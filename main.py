import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title('Jakub Kalamaszek')
    content = """
    Hi, I am Jakub Kalamaszek,  I am 2 degree student of Automation control an Metrology. I'd like to be programmer
    """

    st.info(content)
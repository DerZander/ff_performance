import streamlit as st


def home_index():
    st.title("Home Page")


page_home = st.Page(
    home_index,
    title="Home Page",
    icon="🏠"
)

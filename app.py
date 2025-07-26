import os

import streamlit as st
from dotenv import load_dotenv

from pages.admin import page_question_list, page_question_form
from pages.home import page_home
from pages.questions import page_questions

home_pages = [
    page_home,
]

task_pages = [
    page_questions
]

admin_pages = [
    page_question_list,
    page_question_form
]

pages = {
    "Home": home_pages,
    "Aufgaben": task_pages
}

load_dotenv()
if os.getenv("ENVIRONMENT") != "production":
    pages["Admin"] = admin_pages

if __name__ == "__main__":
    pg = st.navigation(pages)
    pg.run()

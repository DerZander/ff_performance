import os

import streamlit as st
from dotenv import load_dotenv

from pages.admin import page_question_list, page_question_form
from pages.firefighting import page_firefighting
from pages.first_aid import page_first_aid
from pages.home import page_home
from pages.knots_and_stitches import page_knots_and_stitches
from pages.question_exam import page_question_exam
from pages.questions import page_questions
from pages.relay_race import page_relay_race
from pages.technical_assistance import page_technical_assistance

home_pages = [
    page_home,
]

training_pages = [
    page_firefighting,
    page_technical_assistance,
    page_knots_and_stitches,
    page_relay_race,
    page_first_aid,
    page_questions
]

admin_pages = [
    page_question_list,
    page_question_form
]

exam_pages = [
    page_question_exam
]

pages = {
    "Home": home_pages,
    "Aufgaben": training_pages,
    "Wissensabfrage": exam_pages,
}

load_dotenv()
if os.getenv("ENVIRONMENT") != "production":
    pages["Admin"] = admin_pages

if __name__ == "__main__":
    pg = st.navigation(pages)
    pg.run()

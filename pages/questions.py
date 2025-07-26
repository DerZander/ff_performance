import streamlit as st

from services.question_service import get_all_questions


def questions_index():
    st.title("Fragenkatalog")
    st.write("Diese Seite dient zum üben der Fragen.")
    questions_show_all()


def questions_show_all():
    questions = get_all_questions()
    for question in questions:
        question_survey(question)


def question_survey(question=None):
    if question is None:
        return

    expand = st.expander(f"Frage: {question['id']}", icon=":material/info:")
    expand.write(question["title"])

    with expand:
        selected = st.radio("Wähle eine Antwort:", question["answers"], key=f"question_{question['id']}")
        if st.button("Antwort prüfen", key=f"check_{question['id']}"):
            if selected == question["rightAnswer"]:
                st.success("Richtig! 🎉")
            else:
                st.warning(f"Leider falsch. Die richtige Antwort ist: {question['rightAnswer']}")


page_questions = st.Page(questions_index, title="Fragenkatalog", icon="❓")

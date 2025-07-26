import streamlit as st

from services.question_service import get_all_questions

title = "Fragenkatalog"


def index():
    st.title("Fragenkatalog")
    st.markdown(
        """
        Der Fragenkatalog für den Leistungsnachweis 2025 (Stand: 18.03.2025) ist veröffentlicht
        auf der Homepage des VdF NRW e.V.
        Link: https://www.feuerwehrverband.nrw/aktuelles/veranstaltungen/leistungsnachweis \n
        Der vorliegende Fragenkatalog des VdF NRW Fachausschusses Ausbildung und Einsatz
        umfasst nunmehr **30 Fragen** und ist **ein Jahr gültig**. Somit sind **alle** Fragen zu bearbeiten.
        """
    )
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


page_questions = st.Page(
    index,
    title=title,
    icon="❓",
    url_path="/questions",
)

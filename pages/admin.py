import streamlit as st


def question_list():
    st.title("Fragenliste")
    from services.question_service import get_all_questions
    year = st.number_input("Jahr", min_value=2000, max_value=2100, value=2025, step=1)
    questions = get_all_questions(year)
    if not questions:
        st.info("Keine Fragen für dieses Jahr gefunden.")
        return
    for q in questions:
        st.markdown(f"**{q['title']}**")
        for idx, ans in enumerate(q['answers'], 1):
            st.markdown(f"{idx}. {ans}")
        st.markdown(f"**Richtige Antwort:** {q['rightAnswer']}")
        st.divider()


def question_form():
    st.title("Fragenformular")
    from services.question_service import save_question
    year = st.number_input("Jahr", min_value=2000, max_value=2100, value=2025, step=1, key="year_input")
    title = st.text_input("Fragetext", key="title_input")
    answers = []
    for i in range(5):
        answers.append(st.text_input(f"Antwort {i + 1}", key=f"answer_{i}"))
    right_answer = st.selectbox("Richtige Antwort", answers, key="right_answer_select")
    if st.button("Frage speichern", key="save_question_btn"):
        if not title or not all(answers) or not right_answer:
            st.warning("Bitte alle Felder ausfüllen.")
        else:
            from services.question_service import get_all_questions
            existing_questions = get_all_questions(year)
            if any(q["title"].strip().lower() == title.strip().lower() for q in existing_questions):
                st.warning("Diese Frage existiert bereits für das gewählte Jahr.")
            else:
                question = {
                    "title": title,
                    "answers": answers,
                    "rightAnswer": right_answer
                }
                try:
                    save_question(question, year)
                    st.success("Frage erfolgreich gespeichert!")
                    st.session_state.clear()
                except Exception as e:
                    st.error(f"Fehler beim Speichern: {e}")


page_question_list = st.Page(question_list, title="Fragenliste", icon="📋")
page_question_form = st.Page(question_form, title="Fragenformular", icon="✏️")

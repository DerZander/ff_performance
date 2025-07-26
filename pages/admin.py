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
    year = st.number_input("Jahr", min_value=2000, max_value=2100, value=2025, step=1)
    title = st.text_input("Fragetext")
    answers = []
    for i in range(5):
        answers.append(st.text_input(f"Antwort {i + 1}", key=f"answer_{i}"))
    right_answer = st.selectbox("Richtige Antwort", answers)
    if st.button("Frage speichern"):
        if not title or not all(answers) or not right_answer:
            st.warning("Bitte alle Felder ausfüllen.")
        else:
            question = {
                "title": title,
                "answers": answers,
                "rightAnswer": right_answer
            }
            try:
                save_question(question, year)
                st.success("Frage erfolgreich gespeichert!")
            except Exception as e:
                st.error(f"Fehler beim Speichern: {e}")


page_question_list = st.Page(question_list, title="Fragenliste", icon="📋")
page_question_form = st.Page(question_form, title="Fragenformular", icon="✏️")

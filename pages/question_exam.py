import uuid
from datetime import datetime

import streamlit as st

from services.question_service import get_all_questions, get_years, save_difficult_questions

title = "Fragenkatalog - Test"


def index():
    st.title(title)


def question_exam():
    st.title("Prüfungssimulation")
    year = st.selectbox("Jahr", get_years())  # st.number_input("Jahr", min_value=2000, max_value=2100, value=datetime.now().year, step=1, key="exam_year")
    questions = get_all_questions(year)
    if not questions:
        st.info("Keine Fragen für dieses Jahr gefunden.")
        return
    st.write(f"Es werden {len(questions)} Fragen abgefragt.")
    submitted = st.session_state.get("exam_submitted", False)
    # Testlauf-UUID generieren, falls noch nicht vorhanden
    if "test_run_id" not in st.session_state:
        st.session_state["test_run_id"] = str(uuid.uuid4())
    test_run_id = st.session_state["test_run_id"]
    if not submitted:
        user_answers = []
        for idx, q in enumerate(questions):
            user_answer = st.radio(
                f"{idx + 1}. {q['title']}",
                q["answers"],
                key=f"exam_answer_{idx}"
            )
            user_answers.append(user_answer)
        if st.button("Prüfung abgeben"):
            st.session_state["exam_submitted"] = True
            st.session_state["exam_user_answers"] = user_answers
            st.rerun()
    else:
        user_answers = st.session_state.get("exam_user_answers", [])
        score = 0
        difficult_questions = []
        for idx, q in enumerate(questions):
            correct = user_answers[idx] == q["rightAnswer"]
            if correct:
                score += 1
            else:
                from services.question_service import get_answer_id
                given_answer_id = get_answer_id(q["id"], user_answers[idx])
                right_answer_id = get_answer_id(q["id"], q["rightAnswer"])
                difficult_questions.append({
                    "question_id": q["id"],
                    "given_answer_id": given_answer_id,
                    "right_answer_id": right_answer_id,
                    "timestamp": datetime.now().isoformat(),
                    "test_run_id": test_run_id
                })
            st.markdown(f"**{idx + 1}. {q['title']}**")
            st.markdown(f"Deine Antwort: {user_answers[idx]}")
            if correct:
                st.success("Richtig!")
            else:
                st.error(f"Falsch! Richtige Antwort: {q['rightAnswer']}")
            st.divider()
        st.markdown(f"## Ergebnis: {score} von {len(questions)} Punkten")
        if difficult_questions:
            save_difficult_questions(difficult_questions)
        if st.button("Neue Prüfung starten"):
            for idx in range(len(questions)):
                st.session_state.pop(f"exam_answer_{idx}", None)
            st.session_state.pop("exam_submitted", None)
            st.session_state.pop("exam_user_answers", None)
            st.session_state.pop("test_run_id", None)
            st.rerun()


page_question_exam = st.Page(
    question_exam,
    title="Prüfungssimulation",
    icon="📝",
    url_path="/questions_exam",
)

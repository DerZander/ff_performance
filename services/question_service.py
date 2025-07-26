import os
from datetime import datetime

import mariadb
from dotenv import load_dotenv


def get_db_connection():
    load_dotenv()

    # Datenbank-Konfiguration (bitte ggf. anpassen)
    DB_CONFIG = {
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT")),  # Port als Integer
        "database": os.getenv("DB_NAME"),
    }
    try:
        conn = mariadb.connect(**DB_CONFIG)
        return conn
    except mariadb.Error as e:
        raise Exception(f"Fehler beim Verbinden zur MariaDB: {e}. Bitte überprüfe die Umgebungsvariablen.")
        return None


def get_all_questions(year=datetime.now().year):
    conn = get_db_connection()
    if not conn:
        raise Exception("Keine Verbindung zur Datenbank möglich.")
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute(
            "SELECT * FROM questions WHERE year = ?",
            (year,)
        )
        questions = cur.fetchall()
        result = []
        for q in questions:
            # Antworten zur Frage laden
            cur.execute(
                "SELECT id, answer_text FROM answers WHERE question_id = ?",
                (q["id"],)
            )
            answers = cur.fetchall()
            answer_texts = [a["answer_text"] for a in answers]
            right_answer_id = q["right_answer"]
            right_answer = None
            for a in answers:
                if a["id"] == right_answer_id:
                    right_answer = a["answer_text"]
                    break
            result.append({
                "id": q["id"],
                "title": q["title"],
                "answers": answer_texts,
                "rightAnswer": right_answer
            })
        return result
    except mariadb.Error as e:
        print(f"Fehler beim Laden der Fragen: {e}")
        raise
    finally:
        conn.close()


def get_question_by_id(question_id, year=datetime.now().year):
    questions = get_all_questions(year)
    if len(questions) == question_id:
        raise FileNotFoundError(f"No questions found for the year {year}.")
    if question_id < 1 or question_id > len(questions):
        raise IndexError(f"Question ID {question_id} is out of range for the year {year}.")
    return questions[question_id]


def get_random_question(year=datetime.now().year):
    questions = get_all_questions(year)
    if questions:
        import random
        return random.choice(questions)
    return None


def save_question(question, year):
    conn = get_db_connection()
    if not conn:
        raise Exception("Keine Verbindung zur Datenbank möglich.")
    try:
        cur = conn.cursor()
        # 1. Frage speichern
        cur.execute(
            """
            INSERT INTO questions (title, year)
            VALUES (?, ?)
            """,
            (
                question["title"],
                year
            )
        )
        question_id = cur.lastrowid

        # 2. Antworten speichern und ID der richtigen Antwort merken
        right_answer_id = None
        for answer in question["answers"]:
            cur.execute(
                """
                INSERT INTO answers (question_id, answer_text)
                VALUES (?, ?)
                """,
                (question_id, answer)
            )
            answer_id = cur.lastrowid
            if answer == question["rightAnswer"]:
                right_answer_id = answer_id

        # 3. Frage mit ID der richtigen Antwort updaten
        if right_answer_id is not None:
            cur.execute(
                "UPDATE questions SET right_answer = ? WHERE id = ?",
                (right_answer_id, question_id)
            )
        else:
            raise Exception("Richtige Antwort nicht unter den Antworten gefunden!")

        conn.commit()
    except mariadb.Error as e:
        print(f"Fehler beim Speichern der Frage: {e}")
        raise
    finally:
        conn.close()


def get_years():
    conn = get_db_connection()
    if not conn:
        raise Exception("Keine Verbindung zur Datenbank möglich.")
    try:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT year FROM questions ORDER BY year DESC")
        years = [row[0] for row in cur.fetchall()]
        return years
    except mariadb.Error as e:
        print(f"Fehler beim Laden der Jahre: {e}")
        raise
    finally:
        conn.close()


def get_latest_year():
    years = get_years()
    if years:
        return years[0]
    return None


def save_difficult_questions(difficult_questions):
    conn = get_db_connection()
    if not conn:
        raise Exception("Keine Verbindung zur Datenbank möglich.")
    try:
        cur = conn.cursor()
        for entry in difficult_questions:
            cur.execute(
                """
                INSERT INTO difficult_questions (question_id, given_answer_id, right_answer_id, timestamp, test_run_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    entry["question_id"],
                    entry["given_answer_id"],
                    entry["right_answer_id"],
                    entry["timestamp"],
                    entry["test_run_id"]
                )
            )
        conn.commit()
    except mariadb.Error as e:
        print(f"Fehler beim Speichern schwieriger Fragen: {e}")
        raise
    finally:
        conn.close()


def get_answer_id(question_id, answer_text):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT id FROM answers WHERE question_id = ? AND answer_text = ?",
            (question_id, answer_text)
        )
        row = cur.fetchone()
        return row[0] if row else None
    finally:
        conn.close()


if __name__ == "__main__":
    for question in get_all_questions():
        print(f"{question['title']}")

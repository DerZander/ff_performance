import streamlit as st

title = "Erste Hilfe"


def index():
    st.title(title)
    st.markdown(
        """
            Der Übungsteil „Erste Hilfe“ ist von allen Teilnehmern zu absolvieren. 
            
            Im Jahr 2025
            werden folgende Übungen geprüft:
            -  Feststellen der Vitalfunktionen
            -  Stabile Seitenlage
            -  Herz-Lungen-Wiederbelebung
            -  Druckverband am Unterarm
        """
    )


page_first_aid = st.Page(
    index,
    title=title,
    icon="⛑️",
    url_path="/first_aid"
)

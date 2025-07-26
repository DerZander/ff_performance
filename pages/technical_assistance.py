import streamlit as st

title = "Technische Hilfeleistung"


def index():
    st.title(title)
    st.markdown(
        """
        Übung „Person mit Bein unter Container eingeklemmt“ (Staffel: Ohne Ausleuchtung)
        (gemäß Anlage 2 der Richtlinie).
        
        Die Übungen sind entsprechend den gültigen Feuerwehrdienstvorschriften (FwDV)
        durchzuführen. Insbesondere die Regelungen der FwDV 1 und FwDV 3 sowie die
        Unfallverhütungsvorschrift (UVV) Feuerwehren sind zu beachten. Eine detaillierte
        Übungsbeschreibung wird nicht zur Verfügung gestellt.
        """
    )


page_technical_assistance = st.Page(
    index,
    title=title,
    icon="🚒",
    url_path="/technical_assistance"
)

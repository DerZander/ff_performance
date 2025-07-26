import streamlit as st


def firefighting():
    st.title("Brandbekämpfung")
    st.markdown(
        """
        Übung: Vornahme 3 C-Rohre (Staffel: 2 C-Rohre), Offene Wasserentnahmestelle (gemäß
        Anlage 1 der Richtlinie). \n
        Die Übungen sind entsprechend der gültigen Feuerwehrdienstvorschriften (FwDV)
        durchzuführen. Insbesondere die Regelungen der FwDV 1 und FwDV 3 sowie die
        Unfallverhütungsvorschrift (UVV) Feuerwehren sind zu beachten. Die Saugleitung ist mit
        Ventilleine und Halteleine zu sichern. Eine detaillierte Übungsbeschreibung wird nicht
        zur Verfügung gestellt.
        """
    )


page_firefighting = st.Page(
    firefighting,
    title="Brandbekämpfung",
    icon="🔥",
    url_path="/firefighting"
)

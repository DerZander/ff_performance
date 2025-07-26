import streamlit as st

title = "Knoten und Stiche"


def index():
    st.title(title)
    st.markdown(
        """
        Im Jahr 2025 werden folgende Knoten/ Stiche geprüft:
        - Doppelter Ankerstich
        - Zimmermannsschlag
        - Rettungsknoten (Brustbund und Pfahlstich mit Spierenstich)
        
        Alle drei Knoten sind von jedem Teilnehmer innerhalb von drei Minuten zu legen bzw. zu
        stechen.
        """
    )


page_knots_and_stitches = st.Page(
    index,
    title=title,
    icon="🪢",
    url_path="/knots_and_stitches"
)

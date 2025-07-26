import streamlit as st


def home_index():
    st.title("Kreisfeuerwehrtag 2025")
    st.write("Willkommen auf der Hilfsseite für den Kreisfeuerwehrtag 2025!")
    st.write("Auf dieser Seite finden Sie alle wichtigen Informationen und Ressourcen, die Sie benötigen, um sich auf den Tag vorzubereiten.")


page_home = st.Page(
    home_index,
    title="Home",
    icon="🏠"
)

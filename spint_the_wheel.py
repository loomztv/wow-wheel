import streamlit as st
import random

# WoW Daten
wow_data = {
    "Todesritter": ["Blut", "Frost", "Unheilig"],
    "Dämonenjäger": ["Verwüstung", "Rachsucht"],
    "Druide": ["Gleichgewicht", "Wilder Kampf", "Wächter", "Wiederherstellung"],
    "Rufer": ["Verheerung", "Bewahrung", "Optimierung"],
    "Jäger": ["Tierherrschaft", "Treffsicherheit", "Überleben"],
    "Magier": ["Arkan", "Feuer", "Frost"],
    "Mönch": ["Braumeister", "Nebelwirker", "Windläufer"],
    "Paladin": ["Heilig", "Schutz", "Vergeltung"],
    "Priester": ["Disziplin", "Heilig", "Schatten"],
    "Schurke": ["Meucheln", "Gesetzlosigkeit", "Täuschung"],
    "Schamane": ["Elementar", "Verstärkung", "Wiederherstellung"],
    "Hexenmeister": ["Gebrechen", "Dämonologie", "Zerstörung"],
    "Krieger": ["Waffen", "Furor", "Schutz"]
}

# Web-Oberfläche gestalten
st.set_page_config(page_title="WoW Picker", page_icon="🎲")
st.title("🎲 WoW Klassen-Zufallsgenerator")
st.write("Klicke auf den Button, um dein Schicksal zu bestimmen!")

# Button Logik
if st.button("Spin the Wheel!"):
    # Zufallsauswahl
    klasse = random.choice(list(wow_data.keys()))
    spec = random.choice(wow_data[klasse])

    # Anzeige
    st.subheader("Deine Entscheidung:")
    st.success(f"### ⚔️ Klasse: {klasse}")
    st.info(f"### 🛡️ Spezialisierung: {spec}")
    st.balloons()
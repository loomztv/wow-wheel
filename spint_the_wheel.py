import streamlit as st
import random
import time

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

st.set_page_config(page_title="WoW Picker", page_icon="🎲")
st.title("🎲 WoW Klassen-Zufallsgenerator")

if st.button("Rad drehen!"):
    # Platzhalter für die Animation
    slot_container = st.empty()
    
    # Anzahl der Durchläufe
    durchlaeufe = 20
    
    # Animation: Schnell durch die Klassen/Specs wechseln
    for i in range(durchlaeufe):
        klasse = random.choice(list(wow_data.keys()))
        spec = random.choice(wow_data[klasse])
        
        # UI aktualisieren
        slot_container.markdown(f"### 🌀 {klasse} - {spec}")
        
        # Geschwindigkeit steuern (wird zum Ende hin langsamer)
        # i / durchlaeufe sorgt dafür, dass die Wartezeit länger wird
        time.sleep(0.05 + (i / 100))
    
    # Endergebnis
    final_klasse = random.choice(list(wow_data.keys()))
    final_spec = random.choice(wow_data[final_klasse])
    
    # Endergebnis anzeigen
    slot_container.success(f"### 🎉 Deine Wahl: {final_klasse} ({final_spec})")
    st.balloons()

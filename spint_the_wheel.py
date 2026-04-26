import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 WoW Glücksrad")

# HTML/JS für das Glücksrad
wheel_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    #wheel { width: 300px; height: 300px; border-radius: 50%; border: 10px solid #333; position: relative; overflow: hidden; transition: transform 4s cubic-bezier(0.17, 0.67, 0.12, 0.99); }
    .segment { position: absolute; width: 50%; height: 50%; transform-origin: 100% 100%; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: bold; border: 1px solid #fff; box-sizing: border-box; }
</style>
</head>
<body>
    <div id="wheel"></div>
    <button onclick="spin()" style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">Drehen!</button>

    <script>
        const options = ["DK", "DH", "Druide", "Rufer", "Jäger", "Magier", "Mönch", "Paladin", "Priester", "Schurke", "Schamane", "Warlock", "Krieger"];
        const wheel = document.getElementById('wheel');
        const angle = 360 / options.length;

        options.forEach((opt, i) => {
            const div = document.createElement('div');
            div.className = 'segment';
            div.style.transform = `rotate(${i * angle}deg) skewY(${angle - 90}deg)`;
            div.style.backgroundColor = `hsl(${i * 30}, 70%, 70%)`;
            div.innerHTML = `<div style="transform: skewY(${90 - angle}deg) rotate(${angle/2}deg);">${opt}</div>`;
            wheel.appendChild(div);
        });

        function spin() {
            const randomRotation = Math.floor(Math.random() * 3600) + 720;
            wheel.style.transform = `rotate(${randomRotation}deg)`;
        }
    </script>
</body>
</html>
"""

# Das Rad in Streamlit anzeigen
components.html(wheel_html, height=450)

st.write("Drücke den Button im Rad, um es zu drehen!")

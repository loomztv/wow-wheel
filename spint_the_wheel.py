import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 WoW Glücksrad")

# HTML/JS für ein perfekt ausgerichtetes Glücksrad
wheel_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; font-family: sans-serif; }
    #wheel { width: 300px; height: 300px; border-radius: 50%; border: 8px solid #333; position: relative; overflow: hidden; transition: transform 4s cubic-bezier(0.17, 0.67, 0.12, 0.99); }
    .segment { position: absolute; width: 50%; height: 50%; transform-origin: 100% 100%; display: flex; align-items: center; justify-content: center; border-right: 1px solid white; box-sizing: border-box; color: white; font-weight: bold; font-size: 12px; }
</style>
</head>
<body>
    <div id="wheel"></div>
    <br>
    <button onclick="spin()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background: #FFD700; border: none; border-radius: 5px;">Drehen!</button>

    <script>
        const options = ["DK", "DH", "Druide", "Rufer", "Jäger", "Magier", "Mönch", "Paladin", "Priester", "Schurke", "Schamane", "Hexer", "Krieger"];
        const wheel = document.getElementById('wheel');
        const num = options.length;
        const angle = 360 / num;
        
        // Segmente erstellen
        options.forEach((opt, i) => {
            const div = document.createElement('div');
            div.className = 'segment';
            // Mathematik: Wir drehen das Segment und neigen es (skew)
            div.style.transform = `rotate(${i * angle}deg) skewY(${-(90 - angle)}deg)`;
            div.style.backgroundColor = `hsl(${i * (360/num)}, 60%, 50%)`;
            
            // Text ausrichten
            const span = document.createElement('span');
            span.style.transform = `skewY(${90 - angle}deg) rotate(${angle/2}deg)`;
            span.innerText = opt;
            div.appendChild(span);
            wheel.appendChild(div);
        });

        let currentRotation = 0;
        function spin() {
            const randomRotation = Math.floor(Math.random() * 3600) + 720;
            currentRotation += randomRotation;
            wheel.style.transform = `rotate(${currentRotation}deg)`;
        }
    </script>
</body>
</html>
"""

# Rad anzeigen
components.html(wheel_html, height=450)

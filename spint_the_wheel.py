import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 WoW Glücksrad")

# HTML/JS für ein perfekt zentriertes Glücksrad
wheel_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; background-color: #0e1117; color: white; }
    #wheel-container { position: relative; }
    #wheel { cursor: pointer; transition: transform 5s cubic-bezier(0.17, 0.67, 0.12, 0.99); }
    #pointer { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-top: 30px solid #FFD700; z-index: 10; }
    text { user-select: none; pointer-events: none; font-family: 'Arial Black', sans-serif; }
</style>
</head>
<body>
    <div id="wheel-container">
        <div id="pointer"></div>
        <svg id="wheel" width="400" height="400" viewBox="-200 -200 400 400">
            <g id="segments"></g>
        </svg>
    </div>
    <br>
    <button onclick="spin()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background: #FFD700; color: black; border: none; border-radius: 5px; font-weight: bold;">Rad drehen!</button>

    <script>
        const options = ["Krieger", "Paladin", "Jäger", "Schurke", "Priester", "Todesritter", "Schamane", "Magier", "Hexer", "Mönch", "Druide", "Dämonenjäger", "Rufer"];
        const num = options.length;
        const outerRadius = 180;
        const innerRadius = 30; // Platz in der Mitte frei lassen
        const segmentGroup = document.getElementById('segments');

        function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
            const angleInRadians = (angleInDegrees - 90) * Math.PI / 180.0;
            return { x: centerX + (radius * Math.cos(angleInRadians)), y: centerY + (radius * Math.sin(angleInRadians)) };
        }

        for (let i = 0; i < num; i++) {
            const startAngle = i * (360 / num);
            const endAngle = (i + 1) * (360 / num);
            const midAngle = startAngle + (360 / num) / 2;

            // Tortenstück
            const start = polarToCartesian(0, 0, outerRadius, startAngle);
            const end = polarToCartesian(0, 0, outerRadius, endAngle);
            const pathData = `M 0 0 L ${start.x} ${start.y} A ${outerRadius} ${outerRadius} 0 0 1 ${end.x} ${end.y} Z`;

            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
            path.setAttribute("d", pathData);
            path.setAttribute("fill", `hsl(${i * (360/num)}, 70%, 50%)`);
            path.setAttribute("stroke", "white");
            path.setAttribute("stroke-width", "2");
            segmentGroup.appendChild(path);

            // Text
            const className = options[i];
            const letters = className.split("");
            const numLetters = letters.length;
            
            // Verfügbarer Platz für das Wort
            const availableSpace = outerRadius - innerRadius - 20; // 20px Puffer am Rand
            const step = availableSpace / (numLetters + 1);

            for (let j = 0; j < numLetters; j++) {
                // j=0 (erster Buchstabe) beginnt nun weiter außen
                const letterRadius = outerRadius - 20 - (j * step); 
                const textPos = polarToCartesian(0, 0, letterRadius, midAngle);
                
                const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
                text.setAttribute("x", textPos.x);
                text.setAttribute("y", textPos.y);
                text.setAttribute("fill", "white");
                text.setAttribute("font-size", "14");
                text.setAttribute("font-weight", "bold");
                text.setAttribute("text-anchor", "middle");
                text.setAttribute("dominant-baseline", "middle");
                text.textContent = letters[j];
                segmentGroup.appendChild(text);
            }
        }

        let currentRotation = 0;
        function spin() {
            const randomRotation = Math.floor(Math.random() * 3600) + 1440;
            currentRotation += randomRotation;
            document.getElementById('wheel').style.transform = `rotate(${currentRotation}deg)`;
        }
    </script>
</body>
</html>
"""

components.html(wheel_html, height=500)

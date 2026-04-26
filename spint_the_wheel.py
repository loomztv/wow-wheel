import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 WoW Glücksrad")

# HTML/JS mit Ergebnisanzeige
wheel_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; font-family: sans-serif; background-color: #0e1117; color: white; }
    #wheel-container { position: relative; }
    #wheel { cursor: pointer; transition: transform 5s cubic-bezier(0.17, 0.67, 0.12, 0.99); }
    #pointer { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-top: 30px solid #FFD700; z-index: 10; }
    #result { margin-top: 20px; font-size: 24px; font-weight: bold; color: #FFD700; min-height: 30px; }
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
    <div id="result"></div>
    <br>
    <button id="spin-btn" onclick="spin()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background: #FFD700; color: black; border: none; border-radius: 5px; font-weight: bold;">Rad drehen!</button>

    <script>
        const options = ["Krieger", "Paladin", "Jäger", "Schurke", "Priester", "Todesritter", "Schamane", "Magier", "Hexer", "Mönch", "Druide", "Dämonenjäger", "Rufer"];
        const num = options.length;
        const outerRadius = 180;
        const innerRadius = 30;
        const segmentGroup = document.getElementById('segments');
        const wheel = document.getElementById('wheel');
        const resultDiv = document.getElementById('result');
        const spinBtn = document.getElementById('spin-btn');

        function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
            const angleInRadians = (angleInDegrees - 90) * Math.PI / 180.0;
            return { x: centerX + (radius * Math.cos(angleInRadians)), y: centerY + (radius * Math.sin(angleInRadians)) };
        }

        // Rad zeichnen
        for (let i = 0; i < num; i++) {
            const startAngle = i * (360 / num);
            const endAngle = (i + 1) * (360 / num);
            const midAngle = startAngle + (360 / num) / 2;

            const start = polarToCartesian(0, 0, outerRadius, startAngle);
            const end = polarToCartesian(0, 0, outerRadius, endAngle);
            const pathData = `M 0 0 L ${start.x} ${start.y} A ${outerRadius} ${outerRadius} 0 0 1 ${end.x} ${end.y} Z`;

            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
            path.setAttribute("d", pathData);
            path.setAttribute("fill", `hsl(${i * (360/num)}, 70%, 50%)`);
            path.setAttribute("stroke", "white");
            path.setAttribute("stroke-width", "2");
            segmentGroup.appendChild(path);

            const className = options[i];
            const letters = className.split("");
            const numLetters = letters.length;
            const availableSpace = outerRadius - innerRadius - 20;
            const step = availableSpace / (numLetters + 1);

            for (let j = 0; j < numLetters; j++) {
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
            resultDiv.innerText = ""; // Text löschen beim Drehen
            spinBtn.disabled = true;  // Button sperren
            const randomRotation = Math.floor(Math.random() * 3600) + 1440;
            currentRotation += randomRotation;
            wheel.style.transform = `rotate(${currentRotation}deg)`;
        }

        // Event: Wenn die Animation fertig ist
        wheel.addEventListener('transitionend', () => {
            spinBtn.disabled = false;
            // Berechnung: Welches Segment steht am Zeiger?
            const normalizedRotation = currentRotation % 360;
            const sliceAngle = 360 / num;
            // Da das Rad im Uhrzeigersinn dreht, müssen wir die Rotation invertieren um das Segment am Zeiger (oben) zu finden
            const winningIndex = Math.floor(((360 - normalizedRotation) % 360) / sliceAngle);
            resultDiv.innerText = "Du spielst: " + options[winningIndex];
        });
    </script>
</body>
</html>
"""

components.html(wheel_html, height=600)

import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 WoW Glücksrad")

# HTML/JS für das Glücksrad mit horizontalem Text
wheel_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; font-family: sans-serif; background-color: #0e1117; color: white; }
    #wheel { cursor: pointer; transition: transform 5s cubic-bezier(0.17, 0.67, 0.12, 0.99); }
    text { user-select: none; pointer-events: none; font-family: sans-serif; }
</style>
</head>
<body>
    <svg id="wheel" width="400" height="400" viewBox="-200 -200 400 400">
        <g id="segments"></g>
    </svg>
    <br>
    <button onclick="spin()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background: #FFD700; color: black; border: none; border-radius: 5px; font-weight: bold;">Rad drehen!</button>

    <script>
        const options = ["DK", "DH", "Druide", "Rufer", "Jäger", "Magier", "Mönch", "Paladin", "Priester", "Schurke", "Schamane", "Hexer", "Krieger"];
        const num = options.length;
        const radius = 180;
        const segmentGroup = document.getElementById('segments');

        function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
            const angleInRadians = (angleInDegrees - 90) * Math.PI / 180.0;
            return { x: centerX + (radius * Math.cos(angleInRadians)), y: centerY + (radius * Math.sin(angleInRadians)) };
        }

        for (let i = 0; i < num; i++) {
            const startAngle = i * (360 / num);
            const endAngle = (i + 1) * (360 / num);
            const midAngle = startAngle + (360 / num) / 2;

            // Segment Pfad
            const start = polarToCartesian(0, 0, radius, startAngle);
            const end = polarToCartesian(0, 0, radius, endAngle);
            const pathData = `M 0 0 L ${start.x} ${start.y} A ${radius} ${radius} 0 0 1 ${end.x} ${end.y} Z`;

            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
            path.setAttribute("d", pathData);
            path.setAttribute("fill", `hsl(${i * (360/num)}, 70%, 50%)`);
            path.setAttribute("stroke", "white");
            path.setAttribute("stroke-width", "1");
            segmentGroup.appendChild(path);

            // Text - Hier habe ich die Rotation entfernt, damit er horizontal bleibt
            const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
            // Text weiter nach außen setzen (radius * 0.6)
            const textPos = polarToCartesian(0, 0, radius * 0.65, midAngle);
            text.setAttribute("x", textPos.x);
            text.setAttribute("y", textPos.y);
            text.setAttribute("fill", "white");
            text.setAttribute("font-size", "12");
            text.setAttribute("font-weight", "bold");
            text.setAttribute("text-anchor", "middle");
            text.setAttribute("dominant-baseline", "middle");
            // Entfernt: text.setAttribute("transform", `rotate(${midAngle}, ...`); 
            // Jetzt bleibt der Text immer waagerecht
            text.textContent = options[i];
            segmentGroup.appendChild(text);
        }

        let currentRotation = 0;
        function spin() {
            const randomRotation = Math.floor(Math.random() * 3600) + 720;
            currentRotation += randomRotation;
            document.getElementById('wheel').style.transform = `rotate(${currentRotation}deg)`;
        }
    </script>
</body>
</html>
"""

components.html(wheel_html, height=500)

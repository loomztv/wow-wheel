import streamlit as st
import streamlit.components.v1 as components
import random

st.title("🎲 WoW Glücksrad")

# HTML/JS für ein sauberes SVG-Glücksrad
wheel_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; font-family: sans-serif; background-color: #0e1117; color: white; }
    #wheel-container { position: relative; }
    #wheel { cursor: pointer; transition: transform 5s cubic-bezier(0.17, 0.67, 0.12, 0.99); }
    #pointer { position: absolute; top: -10px; left: 50%; transform: translateX(-50%); width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-top: 30px solid #FFD700; z-index: 10; }
</style>
</head>
<body>
    <div id="wheel-container">
        <div id="pointer"></div>
        <svg id="wheel" width="400" height="400" viewBox="-200 -200 400 400">
            </svg>
    </div>
    <br>
    <button onclick="spin()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background: #FFD700; color: black; border: none; border-radius: 5px; font-weight: bold;">Rad drehen!</button>

    <script>
        const options = ["Todesritter", "Dämonenjäger", "Druide", "Rufer", "Jäger", "Magier", "Mönch", "Paladin", "Priester", "Schurke", "Schamane", "Hexer", "Krieger"];
        const num = options.length;
        const wheel = document.getElementById('wheel');
        const angle = 2 * Math.PI / num; // Winkel pro Segment in Radiant

        function describeArc(x, y, radius, startAngle, endAngle){
            const start = polarToCartesian(x, y, radius, endAngle);
            const end = polarToCartesian(x, y, radius, startAngle);
            const largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";
            return ["M", start.x, start.y, "A", radius, radius, 0, largeArcFlag, 0, end.x, end.y, "L", x, y, "Z"].join(" ");
        }

        function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
            const angleInRadians = (angleInDegrees - 90) * Math.PI / 180.0;
            return { x: centerX + (radius * Math.cos(angleInRadians)), y: centerY + (radius * Math.sin(angleInRadians)) };
        }

        // Segmente und Text generieren
        for (let i = 0; i < num; i++) {
            const startAngle = i * (360 / num);
            const endAngle = (i + 1) * (360 / num);
            const d = describeArc(0, 0, 180, startAngle, endAngle); // 180 is the radius

            const group = document.createElementNS("http://www.w3.org/2000/svg", "g");
            
            // Das Segment (Tortenstück)
            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
            path.setAttribute("d", d);
            path.setAttribute("fill", `hsl(${i * (360/num)}, 70%, 50%)`);
            path.setAttribute("stroke", "white");
            path.setAttribute("stroke-width", "1");
            group.appendChild(path);

            // Der Text (Klassenname)
            const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
            text.setAttribute("fill", "white");
            text.setAttribute("font-weight", "bold");
            text.setAttribute("font-size", "14px");
            
            // Text rotieren und positionieren
            const textAngle = startAngle + (360 / num) / 2;
            const textPoint = polarToCartesian(0, 0, 130, textAngle); // Position auf dem Radius (130)
            
            text.setAttribute("x", textPoint.x);
            text.setAttribute("y", textPoint.y);
            text.setAttribute("transform", `rotate(${textAngle}, ${textPoint.x}, ${textPoint.y})`);
            text.setAttribute("text-anchor", "middle"); // Text mittig ausrichten
            text.innerText = options[i];
            
            group.appendChild(text);
            wheel.appendChild(group);
        }

        let currentRotation = 0;
        function spin() {
            // Eine hohe Rotation simuliert das "Drehen"
            const randomRotation = Math.floor(Math.random() * 3600) + 720; // Mind. 2 volle Umdrehungen
            currentRotation += randomRotation;
            wheel.style.transform = `rotate(${currentRotation}deg)`;
        }
    </script>
</body>
</html>
"""

# Rad anzeigen
components.html(wheel_html, height=550)

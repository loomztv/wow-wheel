import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 WoW Spezialisierungs-Rad")

# HTML/JS für das Rad mit 39 Segmenten
wheel_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; background-color: #0e1117; color: white; }
    #wheel-container { position: relative; }
    #wheel { cursor: pointer; transition: transform 6s cubic-bezier(0.17, 0.67, 0.12, 0.99); }
    #pointer { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-top: 30px solid #FFD700; z-index: 10; }
    #result { margin-top: 20px; font-size: 24px; font-weight: bold; color: #FFD700; min-height: 30px; }
    text { user-select: none; pointer-events: none; font-family: 'Arial Black', sans-serif; }
</style>
</head>
<body>
    <div id="wheel-container">
        <div id="pointer"></div>
        <svg id="wheel" width="450" height="450" viewBox="-225 -225 450 450">
            <g id="segments"></g>
        </svg>
    </div>
    <div id="result"></div>
    <br>
    <button id="spin-btn" onclick="spin()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background: #FFD700; color: black; border: none; border-radius: 5px; font-weight: bold;">Rad drehen!</button>

    <script>
        const options = [
            "DK:Blut", "DK:Frost", "DK:Unh", 
            "DH:Verw", "DH:Rach", 
            "Drui:Glei", "Drui:Wild", "Drui:Wäch", "Drui:Wdh", 
            "Rufer:Verh", "Rufer:Bew", "Rufer:Opt",
            "Jäger:Tier", "Jäger:Treff", "Jäger:Über", 
            "Magier:Arka", "Magier:Feuer", "Magier:Frost", 
            "Mönch:Brau", "Mönch:Nebel", "Mönch:Wind", 
            "Pala:Heilig", "Pala:Schutz", "Pala:Verg", 
            "Priester:Disz", "Priester:Heil", "Priester:Schat", 
            "Schurke:Meu", "Schurke:Geset", "Schurke:Täu", 
            "Schama:Elem", "Schama:Verst", "Schama:Wdh", 
            "Hexer:Gebr", "Hexer:Dämo", "Hexer:Zerst", 
            "Krieger:Waff", "Krieger:Fur", "Krieger:Schu"
        ];
        const num = options.length;
        const outerRadius = 210;
        const innerRadius = 40;
        const segmentGroup = document.getElementById('segments');
        const wheel = document.getElementById('wheel');
        const resultDiv = document.getElementById('result');
        const spinBtn = document.getElementById('spin-btn');

        function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
            const angleInRadians = (angleInDegrees - 90) * Math.PI / 180.0;
            return { x: centerX + (radius * Math.cos(angleInRadians)), y: centerY + (radius * Math.sin(angleInRadians)) };
        }

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
            path.setAttribute("stroke-width", "1");
            segmentGroup.appendChild(path);

            const entry = options[i];
            const parts = entry.split(":");
            const textToDisplay = parts[0] + " " + parts[1];
            const letters = textToDisplay.split("");
            const numLetters = letters.length;
            
            // Schriftgröße für 39 Segmente leicht reduziert
            const fontSize = 10; 
            const step = (outerRadius - innerRadius - 20) / (numLetters + 1);

            for (let j = 0; j < numLetters; j++) {
                const letterRadius = outerRadius - 25 - (j * step); 
                const textPos = polarToCartesian(0, 0, letterRadius, midAngle);
                
                const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
                text.setAttribute("x", textPos.x);
                text.setAttribute("y", textPos.y);
                text.setAttribute("fill", "white");
                text.setAttribute("font-size", fontSize);
                text.setAttribute("font-weight", "bold");
                text.setAttribute("text-anchor", "middle");
                text.setAttribute("dominant-baseline", "middle");
                text.textContent = letters[j];
                segmentGroup.appendChild(text);
            }
        }

        let currentRotation = 0;
        function spin() {
            resultDiv.innerText = "";
            spinBtn.disabled = true;
            const randomRotation = Math.floor(Math.random() * 3600) + 1440;
            currentRotation += randomRotation;
            wheel.style.transform = `rotate(${currentRotation}deg)`;
        }

        wheel.addEventListener('transitionend', () => {
            spinBtn.disabled = false;
            const normalizedRotation = currentRotation % 360;
            const sliceAngle = 360 / num;
            const winningIndex = Math.floor(((360 - normalizedRotation) % 360) / sliceAngle);
            resultDiv.innerText = "Spiele: " + options[winningIndex].replace(":", " - ");
        });
    </script>
</body>
</html>
"""

components.html(wheel_html, height=650)

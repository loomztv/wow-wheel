import streamlit as st
import streamlit.components.v1 as components

st.title("🎲 Bleeding Guardians Twink Roulette")

# HTML/JS für das Rad mit zufälliger Anordnung
wheel_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; background-color: #0e1117; color: white; }
    #wheel-container { position: relative; }
    #wheel { cursor: pointer; transition: transform 6s cubic-bezier(0.17, 0.67, 0.12, 0.99); }
    #pointer { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-top: 30px solid #FFD700; z-index: 10; }
    #result { margin-top: 20px; padding: 15px; font-size: 28px; font-weight: bold; color: #FFD700; min-height: 50px; text-align: center; border: 2px solid #FFD700; border-radius: 10px; background-color: #1a1d23; }
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
    <div id="result">Klicke zum Drehen!</div>
    <br>
    <button id="spin-btn" onclick="spin()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background: #FFD700; color: black; border: none; border-radius: 5px; font-weight: bold;">Rad drehen!</button>

    <script>
        const nameMap = {
            "DK Blut": "Todesritter: Blut", "DK Frost": "Todesritter: Frost", "DK Unh": "Todesritter: Unheilig",
            "DH Verw": "Dämonenjäger: Verwüstung", "DH Rach": "Dämonenjäger: Rachsucht", "DH Verschl": "Dämonenjäger: Verschlinger",
            "DW Glei": "Druide: Gleichgewicht", "DW Wild": "Druide: Wilderkampf", "DW Wäch": "Druide: Wächter", "DW Wdh": "Druide: Wiederherstellung",
            "RU Verh": "Rufer: Verheerung", "RU Bew": "Rufer: Bewahrung", "RU Opt": "Rufer: Optimierung",
            "JG Tier": "Jäger: Tierherrschaft", "JG Treff": "Jäger: Treffsicherheit", "JG Über": "Jäger: Überleben",
            "MG Arka": "Magier: Arkan", "MG Feuer": "Magier: Feuer", "MG Frost": "Magier: Frost",
            "MN Brau": "Mönch: Braumeister", "MN Nebel": "Mönch: Nebelwirker", "MN Wind": "Mönch: Windläufer",
            "PL Heil": "Paladin: Heilig", "PL Schut": "Paladin: Schutz", "PL Verg": "Paladin: Vergeltung",
            "PR Disz": "Priester: Disziplin", "PR Heil": "Priester: Heilig", "PR Schat": "Priester: Schatten",
            "SC Meu": "Schurke: Meucheln", "SC Gese": "Schurke: Gesetzlosigkeit", "SC Täu": "Schurke: Täuschung",
            "SM Elem": "Schamane: Elementar", "SM Vers": "Schamane: Verstärkung", "SM Wdh": "Schamane: Wiederherstellung",
            "HX Gebr": "Hexenmeister: Gebrechen", "HX Dämo": "Hexenmeister: Dämonologie", "HX Zers": "Hexenmeister: Zerstörung",
            "KR Waff": "Krieger: Waffen", "KR Fur": "Krieger: Furor", "KR Schut": "Krieger: Schutz"
        };
        
        // Zufalls-Funktion (Fisher-Yates Shuffle)
        function shuffle(array) {
            let currentIndex = array.length, randomIndex;
            while (currentIndex != 0) {
                randomIndex = Math.floor(Math.random() * currentIndex);
                currentIndex--;
                [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
            }
            return array;
        }

        const options = shuffle(Object.keys(nameMap)); // HIER passiert das Zufalls-Mischen
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

        // Segmente zeichnen
        for (let i = 0; i < num; i++) {
            const startAngle = i * (360 / num);
            const midAngle = startAngle + (360 / num) / 2;

            const start = polarToCartesian(0, 0, outerRadius, startAngle);
            const end = polarToCartesian(0, 0, outerRadius, startAngle + (360 / num));
            const pathData = `M 0 0 L ${start.x} ${start.y} A ${outerRadius} ${outerRadius} 0 0 1 ${end.x} ${end.y} Z`;

            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
            path.setAttribute("d", pathData);
            path.setAttribute("fill", `hsl(${i * (360/num)}, 70%, 50%)`);
            path.setAttribute("stroke", "white");
            path.setAttribute("stroke-width", "1");
            segmentGroup.appendChild(path);

            const textToDisplay = options[i];
            const letters = textToDisplay.split("");
            const step = (outerRadius - innerRadius - 40) / (letters.length + 1);

            for (let j = 0; j < letters.length; j++) {
                const letterRadius = outerRadius - 25 - (j * step); 
                const pos = polarToCartesian(0, 0, letterRadius, midAngle);
                
                const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
                text.setAttribute("x", pos.x);
                text.setAttribute("y", pos.y);
                text.setAttribute("fill", "white");
                text.setAttribute("font-size", "11");
                text.setAttribute("font-weight", "bold");
                text.setAttribute("text-anchor", "middle");
                text.setAttribute("dominant-baseline", "middle");
                text.setAttribute("transform", `rotate(${midAngle}, ${pos.x}, ${pos.y})`);
                text.textContent = letters[j];
                segmentGroup.appendChild(text);
            }
        }

        let currentRotation = 0;
        function spin() {
            spinBtn.disabled = true;
            resultDiv.innerText = "Dreht sich...";
            const randomRotation = Math.floor(Math.random() * 3600) + 1440;
            currentRotation += randomRotation;
            wheel.style.transform = `rotate(${currentRotation}deg)`;
        }

        wheel.addEventListener('transitionend', () => {
            spinBtn.disabled = false;
            const normalizedRotation = currentRotation % 360;
            const sliceAngle = 360 / num;
            const winningIndex = Math.floor(((360 - normalizedRotation) % 360) / sliceAngle);
            resultDiv.innerText = "Dein Schicksal: " + nameMap[options[winningIndex]];
        });
    </script>
</body>
</html>
"""

components.html(wheel_html, height=750)

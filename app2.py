# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 00:04:15 2025

@author: march
"""
import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Configuration de la page
st.set_page_config(
    page_title="mme Chaton valentine ?",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Masquer les éléments d'interface de Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stToolbar"] {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ==========================================
# 📸 CONFIGURATION DES PHOTOS 📸
# ==========================================

# 👇 REMPLACE PAR LES NOMS EXACTS DE TES FICHIERS SUR GITHUB 👇
LEFT_IMAGES_FILES = [
    "image.jpg", 
    "2.jpg",
    "3.jpg"
]

RIGHT_IMAGES_FILES = [
    "4.jpg",
    "5.jpg",
    "6.jpg"
]

# Fonction pour lire les images locales
def get_base64_image(image_filename):
    if not os.path.exists(image_filename):
        return None
    with open(image_filename, "rb") as f:
        data = f.read()
    ext = image_filename.split('.')[-1]
    encoded = base64.b64encode(data).decode()
    return f"data:image/{ext};base64,{encoded}"

# Génération du HTML
def generate_img_tags(filenames):
    html = ""
    for filename in filenames:
        img_src = get_base64_image(filename)
        if img_src:
            html += f'<img src="{img_src}" class="side-photo">'
    return html

left_html_content = generate_img_tags(LEFT_IMAGES_FILES)
right_html_content = generate_img_tags(RIGHT_IMAGES_FILES)

# ==========================================
# LE CODE HTML/CSS/JS
# ==========================================

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
    <style>
        body {{
            background-color: #ffe4e1;
            height: 100vh;
            margin: 0;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Pacifico', cursive;
            user-select: none;
        }}

        /* --- STYLES GALERIES --- */
        .gallery {{
            position: fixed;
            top: 0;
            bottom: 0;
            width: 220px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            /* Padding en bas pour ne pas couper la dernière image */
            padding: 20px 20px 150px 20px; 
            overflow-y: auto;
            z-index: 1;
            scrollbar-width: none; 
            -ms-overflow-style: none;
        }}
        .gallery::-webkit-scrollbar {{ display: none; }}

        .gallery-left {{ left: 0; }}
        .gallery-right {{ right: 0; }}

        .side-photo {{
            width: 100%;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            border: 4px solid white;
            transition: transform 0.3s;
            object-fit: cover;
        }}
        
        .side-photo:hover {{
            transform: scale(1.08) rotate(2deg);
            z-index: 2;
        }}

        /* --- JEU CENTRAL --- */
        .game-container {{
            position: relative;
            z-index: 10;
            text-align: center;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}

        h1 {{
            color: #d65db1;
            font-size: 3.5rem;
            text-shadow: 2px 2px #ffc1e3;
            margin-bottom: 40px;
            background-color: rgba(255, 228, 225, 0.9);
            padding: 20px 40px;
            border-radius: 50px;
        }}

        button {{
            font-family: 'Quicksand', sans-serif;
            font-size: 1.6rem;
            padding: 15px 45px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 700;
            transition: all 0.2s;
        }}

        #yesBtn {{
            background-color: #ff69b4; 
            color: white;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.5);
            margin-bottom: 20px;
        }}
        
        #yesBtn:hover {{ transform: scale(1.1); background-color: #ff1493; }}

        #noBtn {{
            background-color: white;
            color: #ff69b4;
            border: 3px solid #ff69b4;
            position: relative; 
            transition: all 0.1s ease;
        }}

        #success-message {{
            display: none;
            color: #d65db1;
            font-size: 2.5rem;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            animation: fadeIn 1s;
        }}

        .initial-position {{ margin-top: 20px; }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* MOBILE */
        @media (max-width: 950px) {{
            .gallery {{ display: none; }}
            h1 {{ font-size: 2rem; padding: 10px 20px; }}
        }}

    </style>
</head>
<body>

    <div class="gallery gallery-left">
        {left_html_content}
    </div>

    <div class="game-container">
        
        <h1 id="main-text">Would you be my Valentine? 🩶</h1>

        <button id="yesBtn" onclick="sheSaidYes()">OUIII 🩶</button>
        
        <div class="initial-position">
            <button id="noBtn" onmouseover="moveButton()" ontouchstart="moveButton()"> non </button>
        </div>

        <div id="success-message">
            MOooohh moi aussi je t'aime mme chaton ! 💖💖<br>
            <span style="font-size: 1.5rem">(De toute façon tu n'avais pas le choix) </span>
        </div>

    </div>

    <div class="gallery gallery-right">
        {right_html_content}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <script>
        const noBtn = document.getElementById('noBtn');
        const yesBtn = document.getElementById('yesBtn');
        const mainText = document.getElementById('main-text');
        const successMsg = document.getElementById('success-message');
        
        let firstMove = true;

        function moveButton() {{
            // Au premier survol, on change le mode de positionnement
            if (firstMove) {{
                noBtn.style.position = 'fixed'; // Permet de bouger partout sur l'écran
                firstMove = false;
            }}

            const windowWidth = window.innerWidth;
            const windowHeight = window.innerHeight;
            const btnWidth = noBtn.offsetWidth;
            const btnHeight = noBtn.offsetHeight;

            // Zones interdites (les galeries)
            // Si écran large, on laisse 250px de chaque côté, sinon 20px
            let sideMargin = windowWidth > 950 ? 250 : 20;

            const maxX = windowWidth - btnWidth - sideMargin;
            const maxY = windowHeight - btnHeight - 20;
            const minX = sideMargin;

            // Calcul aléatoire sûr
            const randomX = Math.max(minX, Math.random() * maxX);
            const randomY = Math.max(20, Math.random() * maxY);

            // Appliquer la nouvelle position
            noBtn.style.left = randomX + 'px';
            noBtn.style.top = randomY + 'px';
        }}

        function sheSaidYes() {{
            // On cache les boutons
            noBtn.style.display = 'none';
            yesBtn.style.display = 'none';
            mainText.style.display = 'none';
            
            // On affiche le message
            successMsg.style.display = 'block';
            document.body.style.backgroundColor = "#ffdae9";

            // Confettis !
            try {{
                confetti({{
                    particleCount: 150,
                    spread: 70,
                    origin: {{ y: 0.6 }},
                    colors: ['#ff69b4', '#ff1493', '#ffffff']
                }});
            }} catch (e) {{}}
        }}
    </script>

</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)






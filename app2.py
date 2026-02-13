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
    "1.jpg", 
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
# LE CODE HTML/CSS/JS ADAPTÉ IPHONE (VERSION CORRIGÉE)
# ==========================================

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
    <style>
        * {{
            box-sizing: border-box;
        }}
        
        body {{
            background-color: #ffe4e1;
            height: 100vh; /* Fallback */
            height: 100dvh; /* Dynamic viewport : s'adapte parfaitement à l'écran mobile réel */
            margin: 0;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Pacifico', cursive;
            user-select: none;
            -webkit-user-select: none; 
            touch-action: none;
        }}

        /* --- STYLES GALERIES (Version PC par défaut) --- */
        .gallery {{
            position: fixed;
            top: 0;
            bottom: 0;
            width: 220px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding: 20px;
            overflow-y: auto;
            z-index: 1;
            scrollbar-width: none; 
        }}
        .gallery::-webkit-scrollbar {{ display: none; }}

        .gallery-left {{ left: 0; }}
        .gallery-right {{ right: 0; }}

        .side-photo {{
            width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border: 3px solid white;
            object-fit: cover;
            transition: transform 0.3s;
        }}

        .side-photo:hover {{
            transform: scale(1.05);
            z-index: 2;
        }}
        
        /* --- JEU CENTRAL --- */
        .game-container {{
            position: relative;
            z-index: 10;
            width: 100%;
            height: 80%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 10px; /* Padding réduit */
        }}

        h1 {{
            color: #d65db1;
            font-size: 3rem;
            text-shadow: 2px 2px #ffc1e3;
            margin-bottom: 30px;
            text-align: center;
            background-color: rgba(255, 228, 225, 0.85);
            border-radius: 30px;
            padding: 15px 30px;
        }}

        button {{
            font-family: 'Quicksand', sans-serif;
            font-size: 1.5rem;
            padding: 15px 35px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 700;
            -webkit-tap-highlight-color: transparent;
        }}

        #yesBtn {{
            background-color: #ff69b4; 
            color: white;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.5);
            margin-bottom: 20px;
            z-index: 20;
        }}

        #noBtn {{
            background-color: white;
            color: #ff69b4;
            border: 2px solid #ff69b4;
            position: relative; 
            transition: top 0.15s, left 0.15s;
            z-index: 20;
        }}

        #success-message {{
            display: none;
            color: #d65db1;
            font-size: 1.8rem;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            animation: fadeIn 1s;
            max-width: 90%;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* ========================================== */
        /* 📱 RESPONSIVE IPHONE / MOBILE 📱           */
        /* ========================================== */
        @media (max-width: 900px) {{
            body {{
                flex-direction: column;
            }}

            /* Bandeaux horizontaux */
            .gallery {{
                position: relative;
                width: 100%;
                height: 150px; /* Hauteur réduite pour gagner de la place */
                flex-direction: row; /* Alignement horizontal */
                
                /* ICI : On centre les photos pour éviter le vide à droite */
                justify-content: center; 
                align-items: center;
                
                top: auto; bottom: auto; left: auto; right: auto;
                padding: 5px;
                overflow-x: auto;
                overflow-y: hidden;
                background-color: rgba(255,255,255,0.4);
                gap: 15px; /* Espace propre entre les photos */
            }}

            .gallery-left {{ order: 1; }}
            .game-container {{ order: 2; flex: 1; }} 
            .gallery-right {{ order: 3; }}

            .side-photo {{
                width: 75px; /* Un tout petit peu plus petit */
                height: 90px;
                flex-shrink: 0;
                border-width: 2px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}

            h1 {{
                font-size: 1.8rem;
                margin-bottom: 15px;
                padding: 10px 20px;
            }}

            button {{
                font-size: 1.2rem;
                padding: 12px 30px;
            }}
            
            #success-message {{
                font-size: 1.3rem;
                padding: 20px;
                margin-top: -20px; /* Remonte un peu le message */
            }}
        }}
    </style>
</head>
<body>

    <div class="gallery gallery-left">
        {left_html_content}
    </div>

    <div class="game-container" id="gameArea">
        
        <h1 id="main-text">Would you be my Valentine? 🩶</h1>

        <button id="yesBtn" onclick="sheSaidYes()">OUIII 🩶</button>
        
        <div class="initial-position">
            <button id="noBtn" onmouseover="moveButton()" ontouchstart="moveButtonTouch(event)"> non </button>
        </div>

        <div id="success-message">
            MOooohh moi aussi je t'aime mme chaton ! 💖💖<br>
            <span style="font-size: 1.2rem; display:block; margin-top:10px">(De toute façon tu n'avais pas le choix) </span>
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
        const gameArea = document.getElementById('gameArea');
        
        let firstMove = true;

        function moveButtonTouch(e) {{
            e.preventDefault(); 
            moveButton();
        }}

        function moveButton() {{
            if (firstMove) {{
                noBtn.style.position = 'fixed'; 
                firstMove = false;
            }}

            const areaRect = gameArea.getBoundingClientRect();
            const btnWidth = noBtn.offsetWidth;
            const btnHeight = noBtn.offsetHeight;

            // Marges de sécurité
            const padding = 15;

            const minX = areaRect.left + padding;
            const maxX = areaRect.right - btnWidth - padding;
            const minY = areaRect.top + padding;
            const maxY = areaRect.bottom - btnHeight - padding;

            const randomX = Math.random() * (maxX - minX) + minX;
            const randomY = Math.random() * (maxY - minY) + minY;

            noBtn.style.left = randomX + 'px';
            noBtn.style.top = randomY + 'px';
        }}

        function sheSaidYes() {{
            noBtn.style.display = 'none';
            yesBtn.style.display = 'none';
            mainText.style.display = 'none';
            
            successMsg.style.display = 'block';
            document.body.style.backgroundColor = "#ffdae9";

            try {{
                var duration = 3000;
                var animationEnd = Date.now() + duration;
                var defaults = {{ startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 }};

                var interval = setInterval(function() {{
                    var timeLeft = animationEnd - Date.now();
                    if (timeLeft <= 0) {{ return clearInterval(interval); }}
                    var particleCount = 50 * (timeLeft / duration);
                    confetti(Object.assign({{}}, defaults, {{ particleCount, origin: {{ x: Math.random(), y: Math.random() - 0.2 }} }}));
                }}, 250);
            }} catch (e) {{}}
        }}
    </script>

</body>
</html>
"""

components.html(html_code, height=700, scrolling=False)









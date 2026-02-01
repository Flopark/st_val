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
    page_title="Valentine ?",
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

# Liste tes fichiers qui sont directement à côté de app.py sur GitHub
# Remplace par les noms EXACTS de tes photos (attention aux majuscules)
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

# Fonction pour lire les images locales et les convertir en base64
def get_base64_image(image_filename):
    if not os.path.exists(image_filename):
        # Si l'image n'est pas trouvée, on ne renvoie rien
        return None
    
    with open(image_filename, "rb") as f:
        data = f.read()
    
    # On récupère l'extension (jpg, png...)
    ext = image_filename.split('.')[-1]
    encoded = base64.b64encode(data).decode()
    return f"data:image/{ext};base64,{encoded}"

# Génération du HTML pour les balises <img>
def generate_img_tags(filenames):
    html = ""
    for filename in filenames:
        img_src = get_base64_image(filename)
        if img_src:
            html += f'<img src="{img_src}" class="side-photo">'
    return html

# Préparation du contenu HTML des galeries
left_html_content = generate_img_tags(LEFT_IMAGES_FILES)
right_html_content = generate_img_tags(RIGHT_IMAGES_FILES)

# ==========================================
# LE CODE HTML/CSS/JS COMPLET
# ==========================================

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
    <style>
        /* Style global du corps de la page */
        body {{
            background-color: #ffe4e1; /* Rose pastel */
            height: 100vh; /* Prend toute la hauteur de la fenêtre */
            margin: 0;
            overflow: hidden; /* Empêche le scroll global de la page */
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Pacifico', cursive;
            user-select: none; /* Empêche la sélection de texte */
        }}

        /* --- STYLES DES GALERIES LATÉRALES --- */
        .gallery {{
            position: fixed;
            top: 0;
            bottom: 0;
            width: 220px; /* Largeur des colonnes photo */
            display: flex;
            flex-direction: column;
            gap: 20px; /* Espace entre les photos */
            
            /* CORRECTION ICI : Padding Haut Droite Bas Gauche */
            /* On met 120px en bas pour être sûr que la dernière image ne soit pas coupée */
            padding: 20px 20px 120px 20px; 
            
            overflow-y: auto; /* Permet le scroll si trop d'images */
            z-index: 1; /* Derrière le jeu */
            
            /* Astuces pour cacher la barre de scroll tout en permettant de scroller */
            scrollbar-width: none; /* Firefox */
            -ms-overflow-style: none; /* IE/Edge */
        }}
        /* Cache la barre de scroll sur Chrome/Safari */
        .gallery::-webkit-scrollbar {{ display: none; }}

        .gallery-left {{ left: 0; }}
        .gallery-right {{ right: 0; }}

        /* Style des photos individuelles */
        .side-photo {{
            width: 100%;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            border: 4px solid white;
            transition: transform 0.3s ease-in-out;
            object-fit: cover; /* S'assure que l'image remplit bien le cadre */
        }}
        
        /* Effet au survol des photos */
        .side-photo:hover {{
            transform: scale(1.08) rotate(2deg);
            z-index: 2;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }}

        /* --- STYLES DU JEU CENTRAL --- */
        .game-container {{
            position: relative;
            z-index: 10; /* Devant les photos */
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
            text-shadow: 3px 3px #ffc1e3;
            margin-bottom: 40px;
            background-color: rgba(255, 235, 240, 0.9);
            padding: 20px 50px;
            border-radius: 60px;
            box-shadow: 0 10px 30px rgba(214, 93, 177, 0.2);
        }}

        /* Style de base des boutons */
        button {{
            font-family: 'Quicksand', sans-serif;
            font-size: 1.6rem;
            padding: 18px 45px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 700;
            transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Effet rebond */
        }}

        /* Le bouton OUI */
        #yesBtn {{
            background: linear-gradient(45deg, #ff69b4, #ff1493);
            color: white;
            box-shadow: 0 6px 20px rgba(255, 105, 180, 0.5);
            margin-bottom: 30px;
        }}
        
        #yesBtn:hover {{ 
            transform: scale(1.15) translateY(-5px); 
            box-shadow: 0 10px 25px rgba(255, 105, 180, 0.7);
        }}

        /* Le bouton NON (fuyant) */
        #noBtn {{
            background-color: white;
            color: #ff69b4;
            border: 3px solid #ff69b4;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            position: absolute; /* Nécessaire pour le mouvement */
        }}

        /* Message de succès final */
        #success-message {{
            display: none; /* Caché au départ */
            color: #d65db1;
            font-size: 2.8rem;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.95);
            padding: 50px 70px;
            border-radius: 40px;
            box-shadow: 0 20px 50px rgba(214, 93, 177, 0.3);
            animation: popIn 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); /* Animation d'apparition */
        }}

        /* Position initiale du bouton Non sous le bouton Oui */
        .initial-position {{ margin-top: 20px; }}

        /* Animation d'apparition du message */
        @keyframes popIn {{
            0% {{ transform: scale(0.5); opacity: 0; }}
            80% {{ transform: scale(1.05); opacity: 1; }}
            100% {{ transform: scale(1); }}
        }}

        /* --- ADAPTATION MOBILE --- */
        /* Sur les écrans de moins de 950px de large (téléphones, petites tablettes) */
        @media (max-width: 950px) {{
            .gallery {{ display: none; }} /* On cache les photos */
            h1 {{ font-size: 2.2rem; padding: 15px 30px; }}
            button {{ font-size: 1.3rem; padding: 15px 35px; }}
            #success-message {{ font-size: 2rem; padding: 30px; }}
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
            <span style="font-size: 1.5rem">(De toutes façon tu n'avais pas le choix) </span>
        </div>
    </div>

    <div class="gallery gallery-right">
        {right_html_content}
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const yesBtn = document.getElementById('yesBtn');
        const mainText = document.getElementById('main-text');
        const successMsg = document.getElementById('success-message');
        
        let firstMove = true;

        // Fonction pour faire bouger le bouton NON
        function moveButton() {{
            // Au premier mouvement, on le passe en position 'fixed' pour qu'il puisse aller partout sur l'écran
            if (firstMove) {{
                noBtn.style.position = 'fixed';
                noBtn.parentElement.style.display = 'none'; // On cache le conteneur initial
                document.body.appendChild(noBtn); // On déplace le bouton directement dans le body
                firstMove = false;
            }}

            // Dimensions de la fenêtre et du bouton
            const windowWidth = window.innerWidth;
            const windowHeight = window.innerHeight;
            const btnWidth = noBtn.offsetWidth;
            const btnHeight = noBtn.offsetHeight;

            // Marge de sécurité latérale pour éviter qu'il n'aille SUR les photos
            // Si écran large (>950px) marge de 250px, sinon marge de 20px
            let sideMargin = windowWidth > 950 ? 250 : 20;

            // Calcul des limites maximales
            const maxX = windowWidth - btnWidth - sideMargin;
            const maxY = windowHeight - btnHeight - 20; // Marge de 20px en bas

            const minX = sideMargin; 

            // Génération de positions aléatoires dans les limites
            const randomX = Math.max(minX, Math.random() * maxX);
            const randomY = Math.max(20, Math.random() * maxY); // Marge de 20px en haut

            // Application des nouvelles coordonnées
            noBtn.style.left = randomX + 'px';
            noBtn.style.top = randomY + 'px';
        }}

        // Fonction déclenchée quand elle clique sur OUI
        function sheSaidYes() {{
            // On cache les boutons et le titre
            noBtn.style.display = 'none';
            yesBtn.style.display = 'none';
            mainText.style.display = 'none';
            
            // On affiche le message de succès
            successMsg.style.display = 'block';
            
            // On change la couleur de fond pour l'ambiance
            document.body.style.backgroundColor = "#ffdae9";
            
            // Lancement de confettis (si la librairie est chargée, sinon ne fait rien)
            try {{
                confetti({{
                    particleCount: 150,
                    spread: 100,
                    origin: {{ y: 0.6 }},
                    colors: ['#ff69b4', '#ff1493', '#ffffff']
                }});
            }} catch (e) {{ console.log("Confetti not loaded"); }}
        }}
    </script>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

</body>
</html>
"""

# Affichage du composant HTML
# Height augmenté à 900 pour être sûr de bien couvrir les grands écrans
components.html(html_code, height=900, scrolling=False)





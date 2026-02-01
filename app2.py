# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 00:04:15 2025

@author: march
"""
import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(
    page_title="Valentine ?",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# On cache les éléments de l'interface Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stToolbar"] {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Le code HTML/JS/CSS
html_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@500&display=swap" rel="stylesheet">
    <style>
        /* On empêche le scroll pour que tout reste propre */
        body {
            background-color: #ffe4e1; /* Rose pastel */
            height: 100vh;
            margin: 0;
            overflow: hidden; 
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Pacifico', cursive;
            user-select: none; /* Empêche de sélectionner le texte */
        }

        h1 {
            color: #d65db1;
            font-size: 3rem; /* Un peu plus petit pour le mobile */
            text-shadow: 2px 2px #ffc1e3;
            margin-bottom: 40px;
            text-align: center;
            z-index: 10;
        }

        .container {
            position: relative;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        button {
            font-family: 'Quicksand', sans-serif;
            font-size: 1.5rem;
            padding: 15px 40px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.1s ease; /* Transition très rapide */
        }

        /* Le bouton OUI reste centré et stable */
        #yesBtn {
            background-color: #ff69b4; 
            color: white;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.4);
            z-index: 5;
            margin-bottom: 20px; /* Espace si les boutons sont l'un sous l'autre */
        }

        #yesBtn:hover {
            transform: scale(1.1);
            background-color: #ff1493;
        }

        /* Le bouton NON */
        #noBtn {
            background-color: white;
            color: #ff69b4;
            border: 2px solid #ff69b4;
            position: absolute; /* Absolu pour pouvoir bouger partout */
            z-index: 5;
        }

        /* Message final */
        #success-message {
            display: none;
            color: #d65db1;
            font-size: 2.5rem;
            text-align: center;
            animation: fadeIn 1s;
            z-index: 20;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Conteneur pour centrer le bouton NON au départ */
        .initial-position {
            margin-top: 20px;
        }

    </style>
</head>
<body>

    <div class="container">
        <h1 id="main-text">Would you be my Valentine? 💖</h1>

        <button id="yesBtn" onclick="sheSaidYes()">YES 🥰</button>
        
        <div class="initial-position">
            <button id="noBtn" onmouseover="moveButton()" onclick="moveButton()">NO 😢</button>
        </div>

        <div id="success-message">
            Yayyy !! 💖 Je t'aime !<br>
            <span style="font-size: 1.5rem">C'était le seul choix possible 😎</span>
        </div>
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const yesBtn = document.getElementById('yesBtn');
        const mainText = document.getElementById('main-text');
        const successMsg = document.getElementById('success-message');
        
        let firstMove = true;

        function moveButton() {
            // Si c'est le premier mouvement, on change la position en 'absolute' par rapport au body
            if (firstMove) {
                noBtn.style.position = 'fixed'; // Fixed garantit que c'est relatif à la fenêtre vue
                firstMove = false;
            }

            // Récupérer la taille de la fenêtre
            const windowWidth = window.innerWidth;
            const windowHeight = window.innerHeight;

            // Récupérer la taille du bouton
            const btnWidth = noBtn.offsetWidth;
            const btnHeight = noBtn.offsetHeight;

            // Calculer la zone libre (fenêtre - taille bouton - petite marge de sécurité de 20px)
            const maxX = windowWidth - btnWidth - 20;
            const maxY = windowHeight - btnHeight - 20;

            // Générer des coordonnées aléatoires dans cette zone
            const randomX = Math.random() * maxX;
            const randomY = Math.random() * maxY;

            // Appliquer les nouvelles positions (avec une marge min de 10px pour ne pas coller au bord gauche/haut)
            noBtn.style.left = Math.max(10, randomX) + 'px';
            noBtn.style.top = Math.max(10, randomY) + 'px';
        }

        function sheSaidYes() {
            // Cacher les boutons et le texte
            noBtn.style.display = 'none';
            yesBtn.style.display = 'none';
            mainText.style.display = 'none';
            
            // Afficher le message
            successMsg.style.display = 'block';
            
            // Changer la couleur de fond
            document.body.style.backgroundColor = "#ffcce0";
        }
    </script>

</body>
</html>
"""

# Hauteur 850 pour être sûr de prendre tout l'écran d'un mobile ou laptop standard
components.html(html_code, height=850, scrolling=False)

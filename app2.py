# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 00:04:15 2025

@author: march
"""
import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(
    page_title="Pour ma Valentine 💖",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Masquer le menu hamburger et le footer de Streamlit pour faire plus "pro"
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Le code HTML/JS qui gère tout le visuel et l'animation
html_code = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@500&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #ffe4e1; /* Rose pastel misty rose */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
            font-family: 'Pacifico', cursive;
        }

        h1 {
            color: #d65db1;
            font-size: 3.5rem;
            text-shadow: 2px 2px #ffc1e3;
            margin-bottom: 50px;
            text-align: center;
        }

        .buttons {
            position: relative;
            width: 100%;
            height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
        }

        button {
            font-family: 'Quicksand', sans-serif;
            font-size: 1.5rem;
            padding: 15px 40px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            position: absolute; /* Important pour le mouvement */
        }

        #yesBtn {
            background-color: #ff69b4; /* Hot pink */
            color: white;
            position: relative; /* Le bouton Oui reste fixe par rapport au flux */
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.4);
        }

        #yesBtn:hover {
            transform: scale(1.1);
            background-color: #ff1493;
        }

        #noBtn {
            background-color: white;
            color: #ff69b4;
            border: 2px solid #ff69b4;
            left: 55%; /* Position initiale à droite du bouton Oui */
        }

        /* Message de succès caché au début */
        #success-message {
            display: none;
            color: #d65db1;
            font-size: 2rem;
            margin-top: 20px;
            text-align: center;
            animation: popIn 0.5s ease-out;
        }

        @keyframes popIn {
            0% { transform: scale(0); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }

    </style>
</head>
<body>

    <h1 id="main-text">Would you be my Valentine? 💖</h1>

    <div class="buttons">
        <button id="yesBtn" onclick="sheSaidYes()">YES 🥰</button>
        <button id="noBtn" onmouseover="moveButton()" onclick="moveButton()">NO 😢</button>
    </div>

    <div id="success-message">
        Yaaaaay ! Je t'aime ! 💖💑<br>
        (Rendez-vous le 14 !)
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const yesBtn = document.getElementById('yesBtn');
        const mainText = document.getElementById('main-text');
        const successMsg = document.getElementById('success-message');

        function moveButton() {
            // Calculer les dimensions de la fenêtre visible
            const x = Math.random() * (window.innerWidth - noBtn.offsetWidth);
            const y = Math.random() * (window.innerHeight - noBtn.offsetHeight);
            
            // Appliquer les nouvelles coordonnées
            noBtn.style.position = 'absolute';
            noBtn.style.left = `${x}px`;
            noBtn.style.top = `${y}px`;
        }

        function sheSaidYes() {
            // Faire disparaître les boutons
            noBtn.style.display = 'none';
            yesBtn.style.display = 'none';
            mainText.style.display = 'none';
            
            // Afficher le message
            successMsg.style.display = 'block';
            
            // Lancer des confettis (effet simple via changement de couleur de fond rapide ou alert)
            document.body.style.backgroundColor = "#ffcce0";
        }
    </script>

</body>
</html>
"""

# Affichage du composant HTML en plein écran
components.html(html_code, height=800, scrolling=False)
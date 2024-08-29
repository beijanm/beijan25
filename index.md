---
layout: base
title: Student Home 
description: Home Page
hide: true
---
Beijan's student repository


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NBA Player Picker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: black; /* Black background as per your layout */
            color: white; /* White text for visibility */
            text-align: center;
            margin: 0;
            padding: 20px;
        }

        #player-picker-container {
            background-color: #333;
            padding: 20px;
            margin: 50px auto;
            width: 300px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
        }

        #player-image {
            width: 100%;
            height: auto;
            border-radius: 10px;
        }

        #player-name {
            margin-top: 15px;
            font-size: 1.5em;
            color: #FFD700; /* Gold color for player name */
        }

        #choose-player-btn {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #FFD700; /* Matching the player name color */
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            color: black;
        }

        #choose-player-btn:hover {
            background-color: #FFA500; /* Darker gold on hover */
        }
    </style>
</head>
<body>
    <h1>NBA Player Picker</h1>
    <div id="player-picker-container">
        <img id="player-image" src="" alt="NBA Player">
        <p id="player-name">Click the button to choose a player!</p>
        <button id="choose-player-btn">Choose Player</button>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const players = [
                {
                    name: "LeBron James",
                    image: "https://example.com/lebron.jpg"
                },
                {
                    name: "Stephen Curry",
                    image: "https://example.com/curry.jpg"
                },
                {
                    name: "Kevin Durant",
                    image: "https://example.com/durant.jpg"
                },
                {
                    name: "Giannis Antetokounmpo",
                    image: "https://example.com/giannis.jpg"
                },
                {
                    name: "Luka Dončić",
                    image: "https://example.com/luka.jpg"
                }
            ];

            const playerImage = document.getElementById('player-image');
            const playerName = document.getElementById('player-name');
            const choosePlayerBtn = document.getElementById('choose-player-btn');

            choosePlayerBtn.addEventListener('click', function() {
                const randomIndex = Math.floor(Math.random() * players.length);
                const chosenPlayer = players[randomIndex];

                playerImage.src = chosenPlayer.image;
                playerName.textContent = chosenPlayer.name;
            });
        });
    </script>
</body>
</html>


# Snake-Game-HS2021

Project Language: Python

Group ID:  108

## Table of contents
* [Introduction](#Introduction)
* [Project-Description](#Project-Description)
* [Repository](#Repository)
* [Installations](#Installations)
* [How-to-Play](#How-to-Play)


## Introduction
This project is part of the mandatory curriculum of the course “7,789 | 8,789: Skills: Programming with Advanced Computer Languages” supervised by Dr. Mario Silic at the University of St. Gallen. It was created by a group of students consisting of six people namely Deniz Süzen (17-609-066), Hyungmin Koh (13-615-893), Jonas Rusca (17-606-997), Nurel Yilmaz (15-608-458), Samuel Bissegger (15-714-736) and Wei Zheng (15-617-400).


## Project-Description
This project aims to build a simple and fun “Snake” game with some individualized features using the programming language Python. Snake is a bordered plane game, designed in the time of the arcade game blockade in the late 1970ies. The game design is set up to maneuver three dots, and later a growing line in direction of tokens. The objective of the game is to eat as many tokens as possible. At the same time, the player must not touch the walls or collide with the player's avatar itself. Else the game ends and the player is forced to attempt anew. We decided on applying both features, the collision with the border of the window and the avatar itself.

To the ends of the creation of the game, Pygame was utilized. PyGame is an open-source library that is designed for making video games. It has inbuilt graphics and sound libraries. 

The game starts with a title screen where the user can refer to the “instructions” if needed. To start the game, the player has to press “Play”. To leave the game, the player just has to close the window. 

![Main_Menu](https://user-images.githubusercontent.com/95411649/147395033-027b0334-68f8-4c7e-875d-bca1fac15532.png)

![Instructions](https://user-images.githubusercontent.com/95411649/147395008-8b8c1974-fd0e-42a5-858b-2778bd32d376.png)

The gaming interface shows the score at the top left corner. To play the game the user steers the snake, which is the green line consisting of 3 blocks, using the arrow keys. We based our code on various codes from different creators, such as Wajiha Urooj (https://www.edureka.co/blog/snake-game-with-pygame/), kiteco (https://github.com/kiteco/python-youtube-code) and Grape Juice (https://dev.to/grapejuice/getting-started-with-pygame-making-a-snake-game-2i1g). In addition to the base code, we have implemented **five additional features**: 

* First, we created a title screen that shows the main menu with 2 buttons “Play” and “Instructions”. When you click on instructions, it shows the color and score properties of the foods.
* Second is the feature of the two types of “food” added to the game. Starting with the regular red food item that increases the length of the body by 1 block and the score by 1 point after being eaten. The other is a special item that increases the length of the snake by 3 blocks but also increases the score by 5 extra points and is colored yellow.
* Third is the background music added which loops throughout the game. 
* Fourth is the chessboard-like background.  
* Fifth are sound effects played once a food item is eaten or when the snake collides with itself or the boundary. 

![Screen Shot 2021-12-22 at 6 04 14 PM](https://user-images.githubusercontent.com/95411649/147129734-70e7d2b5-4904-43d9-8158-c01ba53d5260.png)

Once the snake runs into the border or into itself, the game over screen pops up and shows the reached score. The player can choose to restart the game by clicking the “play game” button or choose to exit the game by selecting “quit game” or closing the window directly. 

## Repository
The repository shows 5 files. The “README.md” file gives an overall introduction and project description with screenshots showing the gaming interfaces. “Snake-Game-HS2021.py” contains the code. “Ding.mp3” and “game_over.mp3” are used for the sound effects. “Snake Game – Theme Song.mp3” is used for the background music. 

In case you are using jupyter notebook to run the code, please ensure that the code, sound, and background music files are located in the same folder for the code to run smoothly. 

## Installations
The following programs were used to analyse and test the code:
* Python 3.9 
* Anaconda 3
* Jupyter Notebook and VS Code (visual studio code - program)

The following packages and modules are REQUIRED to run the code: 
* pygame, time, sys, random, typing

In case these packages are not installed yet, please run “pip install” for each package. If pip is not installed yet, please run "python get-pip.py" first.
* pip install pygame
* pip install random

## How-to-Play
1. Download the program (along with sounds from our Github account). Go to the link https://github.com/WeiZ8/Snake-Game-HS2021.git 
2. Fork the repository
3. After downloading, load the folder in your code editor like VS Code, PyCharm, etc. 
4. Run the file snake.py 
5. For moving the snake use the arrow buttons only.

You are all set now to play. 
Enjoy the game!

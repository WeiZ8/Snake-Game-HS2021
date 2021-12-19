# Snake-Game-HS2021

Project Language: Python

Group ID:  108

## Table of contents
* [Introduction](#Introduction)
* [Project-Description](#Project-Description)
* [Repository](#Repository)
* [Installations](#Installations)

## Introduction
This project is part of the mandatory curriculum of the course “7,789 | 8,789: Skills: Programming with Advanced Computer Languages” supervised by Dr. Mario Silic at the University of St. Gallen. It was created by a group of students consisting of six people namely Deniz Süzen, Hyungmin Koh, Jonas Rusca, Nurel Yilmaz, Samuel Bissegger und Wei Zheng. 


## Project-Description
This project aims to build a simple and fun “Snake” game with some individualized features using the programming language Python. Snake is a bordered plane game, designed in the time of the arcade game blockade in the late 1970ies. The game design is set up to maneuver a dot, and later a line in direction of tokens. The tokens have the impact of making the line grow in length. The objective of the game is to eat as many tokens as possible. At the same time, the player must not touch the walls, the obstacle, or collide with the player's avatar itself. Else the game ends and the player is forced to attempt anew. 

We will be using Pygame and pygame_menu to create this game. PyGame is an open-source library that is designed for making video games. It has inbuilt graphics and sound libraries. It is also beginner-friendly and is suitable for cross-platform games. PyGame-Menu is a pygame-complementary library, which supports various buttons, labels, color inputs, and text inputs. 


![Snake Game_Main Menu](https://user-images.githubusercontent.com/95411649/146671962-eff85403-b84a-43d2-b9b0-8d03ac6cc1e8.png)

The game starts with a title screen where the user can enter their name and refer to the instructions if needed. To start the game, the player has to press “start” or press “quit”, if they wish to leave the game.

![Snake Game_Main Game](https://user-images.githubusercontent.com/95411649/146672012-7416a006-9227-4173-8ac3-b21b15ec76e5.png)

The gaming interface shows the score at the top left corner. To play the game the user navigates the snake, which is the green block, using the arrow keys. There are three additional features on the screen. First are the obstacles which are colored in black and should be avoided. The other two features are the two types of “food” added to the game. Starting with the regular red food item that increases the length of the body by 1 block and the score by 1 point after being eaten. The other is a special item that appears randomly after 15 seconds. The yellow food block increases the length of the snake by 5 blocks but also increases the score by 3 extra points. A sound effect is played once a food item is eaten or when the snake collides with the obstacle, the wall, or itself. 

![Snake_Game Over](https://user-images.githubusercontent.com/95411649/146673326-0989190d-8af0-4e14-9d3d-30835167e658.png)

Once the snake runs into an obstacle, the border or the avatar itself, the game over screen pops up and shows the reached score. The player can choose to restart the game by clicking the “replay game” button or choose to exit the game by selecting “quit game”. 

## Repository
The repository shows five files. The “README.md” file gives an overall introduction and project description. “Snake-Game-HS2021.py” contains the code. The screenshots within “Screenshot” show the gaming interfaces. “Ding.mp3” and “game_over.mp3” are used for the sound effects. 

In case you are using jupyter notebook to run the code, please ensure that the code and the sound files are located in the same folder for the code to run smoothly. 

## Installations
The following programs were used to analyse and test the code:
* Python 3.9 
* Anaconda 3
* Jupyter Notebook and VS Code (visual studio code - program)

The following packages are REQUIRED to run the code: 
* pygame, pygame-menu, time, datetime, sys, random

In case these packages are not installed yet, please run “pip install” for each package.

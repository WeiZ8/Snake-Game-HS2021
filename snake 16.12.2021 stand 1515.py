# Snake game with additional features

'''
About the Project

This project aims to build a simple and fun “Snake” game with some individualized features using the programming language Python. Snake is a bordered plane game, designed in the time of the arcade game blockade in the late 1970ies. The game design is set up to maneuver a dot, and later a line in direction of tokens. The tokens have the impact of making the line grow in length. The objective of the game is to eat as many tokens as possible. At the same time, the player must not touch the walls, the obstacle, or collide with the player's avatar. Else the game ends and the player is attempt anew. 

We will be using Pygame and pygame.menu to create this game. PyGame is an open-source library that is designed for making video games. It has inbuilt graphics and sound libraries. It is also beginner-friendly and is suitable for cross-platform games.

The game starts with a title screen where the user can enter their name and refer to the instructions if needed. To start the game the player has to press “start” or press “quit” if they wish to leave the game.

The gaming interface shows the score at the top left corner. To play the game the user navigates the snake, which is the green block, with the arrow keys. There are three additional features on the screen. First are the obstacles which are colored in black and should be avoided. The other two features are the two types of “food” added to the game. Starting with the regular red food item that increases the length of the body by one block and the score by 1 point after being eaten. The other is a special item that appears randomly after 15 seconds. The yellow food block increases the length of the snake by 5 blocks but also increases the score by three extra points. A sound effect is played once a food item is eaten or when the snake collides with the obstacle, the wall, or itself.

Once you run into an obstacle, the border or the avatar itself, the game over screen pops up and shows the currently reached score. The player can choose to restart the game by clicking the “replay game” button or choose to exit the game by selecting “quit game”. 
'''

'''
Prequisites

The following packages are required and need to be installed:
* pygame
* pygame_menu
* time
* dateime
* sys, random
Please run “pip install” for each package. In case pip is not installed yet, please run "python get-pip.py" first.
'''


#Import the necessary libararies.

#Pygame is a programming language library in python with which games can be programed. Import pygame to get started. 
import pygame
from pygame import mixer
import pygame_menu

#Import time module to set the speed for the snake.
import time

#Import datetime for time measurement.
import datetime

#Import the random module so that the food which the snake eats will appear at random locations on the display.
import sys, random

#Before we can do much with pygame, we  need to initialize it. This is done by pygame.init() which initializes all imported pygame modules. 
pygame.init()

#------------------[Settings]---------------------

#The color scheme used in Pygame is RGB i.e “Red Green Blue”. If we set all these to 0’s, the color will be black and all 255’s will be white. Here we have defined a few colors.

RED = (175, 0, 42)
BLUE = (240, 248, 255)
DARKBLUE = (61, 90, 110)
GREEN = (0, 128, 0)
YELLOW = (255, 165, 0)
BLACK = (0, 0, 0)


#Next we create two variables for our screen. For that we define the width and the height of the screen. 
DIS_WIDTH = 800
DIS_HEIGHT = 600

#To create an actual screen with Pygame we make use of the display.set_mode() function. At the same time, we use the above-defined width and height. 
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
#We want to give the pygame window by labeling it "Snake Game". This is done by using the code below. 
pygame.display.set_caption('Snake Game')

#To keep track of the time we create an object named "clock". 
#Initializing pygame.time.Clock() which controls how many times per second our game loop should run. 
CLOCK = pygame.time.Clock()
 
#We define the size of the snake.
snake_block = 10
#We define the speed of the snake.
snake_speed_general = 30 



#we now choose and define the font.
font_style = pygame.font.SysFont("comicsans", 25)
score_font = pygame.font.SysFont("comicsans", 25)
# As part of the fonts we also import our menu fonts (from pygame_menu).
font_menu = pygame_menu.font.FONT_8BIT

#------------------[The Menu]---------------------
#Main_Menu
def main_menu():
   
    def start_the_game():
        gameLoop()
        # Do the job here !
        pass

    menu = pygame_menu.Menu(width=DIS_WIDTH, height=DIS_HEIGHT, title='Welcome',
        theme=pygame_menu.themes.THEME_DARK);

    menu.add.text_input('Name : ', default='John Doe')
    menu.add.button('Play', start_the_game, font_name = font_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT, font_name = font_menu)
    menu.mainloop(DIS)


#End menu
def show_end_screen(game_score, DIS_WIDTH, DIS_HEIGHT, replay, window):
   end_menu = pygame_menu.Menu(width=DIS_WIDTH, height=DIS_HEIGHT, title='Game Over', 
   theme=pygame_menu.themes.THEME_DARK);
   end_menu.add.label("Your Score: " + str(game_score), font_name = font_menu)
   end_menu.add.button("Replay Game", replay, font_name = font_menu)
   end_menu.add.button("Quit Game", pygame_menu.events.EXIT, font_name = font_menu)
   end_menu.mainloop(window)
       
 
#We are adding a starting score 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, DARKBLUE)
    DIS.blit(value, [0, 0])
   
 
#Now we create the snake. It will be represented as a rectangle. To draw rectangles in Pygame, we  make use of the function called draw.rect() which will help us draw the rectangle with the desired color and size. 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(DIS, GREEN, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    DIS.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])
       

def gameLoop():
    game_over = False
    game_close = False
 
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

#The variables x1_change and y1_change hold the updating values of the x and y coordinates.  
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    extra_points = 0
    

    #PH: Define the time related to the randomized appearance of the specialfood.
    last_specialfood_time = datetime.datetime.now()
    spc_foods = []
    SPECIAL_FOOD_LIFETIME = 5 #seconds, if SPECIAL_FOOD_LIFETIME <= SPECIAL_FOOD_BACKOFF, we might not have multiple special foods at same time
    SPECIAL_FOOD_BACKOFF = 10 #seconds, how much time between two special foods spawns
    SPECIAL_FOOD_SPAWN_CHANCES = 1 #1/SPECIAL_FOOD_SPAWN_CHANCES to spawn, given time is bigger than backoff
    MAX_SPECIAL_FOOD_COUNT = 1 #maximum amount of special foods we want, at any given time
    
    #The snake game includes food for the snake. So the food needs to be first created. 
    #Define the randomized apperance of the food items within the display and its size
    foodx = round(random.randrange(40, DIS_WIDTH - 40) / 10.0) * 10.0
    foody = round(random.randrange(40, DIS_HEIGHT - 40) / 10.0) * 10.0
    specialfoodx = round(random.randrange(40 , DIS_WIDTH - 40) / 10.0) * 10.0
    specialfoody = round(random.randrange(40, DIS_HEIGHT - 40) / 10.0) * 10.0 
   
 #task1 from Deniz: obstacle needs to be defined
    obstaclex = round(random.randrange (40 , DIS_WIDTH - 40) / 10.0) * 10.0
    obstacley = round(random.randrange(40, DIS_HEIGHT - 40) / 10.0) * 10.0

#------------------[GAME LOGIC]---------------------
 #our infinite game loop
    while not game_over:
 
        while game_close == True:
            #the display screen is changed from the default black to blue using the fill() method.
            show_end_screen(str(Length_of_snake-1), DIS_WIDTH, DIS_HEIGHT, gameLoop, DIS)
           
            #We want to display the score of the player. To do this, we created the function “Your_score”. This function will display the length of the snake subtracted by 1 because that is the initial size of the snake.
            Your_score(Length_of_snake - 1 + extra_points)
            pygame.display.update()
 
#To move the snake, we use the key events present in the KEYDOWN class of Pygame. The events that are used over here are K_UP, K_DOWN, K_LEFT, and K_RIGHT to make the snake move up, down, left and right respectively. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        #When the user moves the snake by pressing the key we want the snake to move with the general speed defined with 15.            
        CLOCK.tick(snake_speed_general)        

        #if players hits the boundaries of the screen, then they lose. The ‘if’ statement defines the limits for the x and y coordinates of the snake to be less than or equal to that of the screen.
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
            #sound integration
            game_over_Sound = mixer.Sound('game_over.mp3')
            game_over_Sound.play()
        x1 += x1_change
        y1 += y1_change

        #the display screen is changed from the default black to blue using the fill() method.
        DIS.fill(BLUE)
        
        ##task 2 from Deniz: obstacle need to be drawn
        pygame.draw.rect(DIS, BLACK, [obstaclex, obstacley, snake_block, snake_block])
        
        #the food is created, colored and shaped 
        pygame.draw.rect(DIS, RED, pygame.Rect(foodx, foody,snake_block, snake_block),40, 5)
       
        #this is created for the special food.
        #PH: we always draw all special foods that are not older than 10s
        for fd in spc_foods:
            special_food_x = fd[0]
            special_food_y = fd[1]
            time = fd[2]
            time_delta = datetime.datetime.now() - time
            if time_delta.seconds > SPECIAL_FOOD_LIFETIME:
                continue
            else:   
                pygame.draw.rect(DIS, YELLOW, pygame.Rect(specialfoodx, specialfoody,snake_block, snake_block),40, 5)
        
        #PH: Should we generate new special food?
        # 1 in 3 chances every 2 seconds
        time_delta = datetime.datetime.now() - last_specialfood_time
        rnd = random.randint(1,SPECIAL_FOOD_SPAWN_CHANCES)
        #PH 1 in 3 chances that special food spawns
        if  rnd == 1 and time_delta.seconds >SPECIAL_FOOD_BACKOFF and len(spc_foods)<= MAX_SPECIAL_FOOD_COUNT:
            last_specialfood_time = datetime.datetime.now()
            specialfoodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 10.0) * 10.0
            specialfoody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 10.0) * 10.0 
            spc_foods.append([specialfoodx, specialfoody, last_specialfood_time])
        

        #The following code increases the size of the snake when it eats the food. The length of the snake is basically contained in a list and the initial size that is specified in the following code is one block.
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                #sound integration
                game_over_Sound = mixer.Sound('game_over.mp3')
                game_over_Sound.play()
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1 + extra_points)
 
        pygame.display.update()
 
        #foods pop up randomly within the window and adds to the length of the snake after being eaten
        if x1 == foodx and y1 == foody:
            #sound integration
            ding_Sound = mixer.Sound('Ding.mp3')
            ding_Sound.play()
            foodx = round(random.randrange(40 , DIS_WIDTH - 40) / 10.0) * 10.0
            foody = round(random.randrange(40 , DIS_HEIGHT - 40) / 10.0) * 10.0
            # if food is eaten, it increases the length by 1 block
            Length_of_snake += 1
            
  ##task 3 from Deniz: in case snake eats obstacle snake dies
        if x1 == obstaclex and y1 == obstacley:
            foodx = round(random.randrange(40 , DIS_WIDTH - 40) / 10.0) * 10.0
            foody = round(random.randrange(40 , DIS_HEIGHT - 40) / 10.0) * 10.0
            game_close = True
            #sound integration
            game_over_Sound = mixer.Sound('game_over.mp3')
            game_over_Sound.play()
 
        #the special food pops up on the display at random locations. 
        if x1 == specialfoodx and y1 == specialfoody:
            #sound integration
            ding_Sound = mixer.Sound('Ding.mp3')
            ding_Sound.play()
            specialfoodx = round(random.randrange(40 , DIS_WIDTH - 40) / 10.0) * 10.0
            specialfoody = round(random.randrange(40 , DIS_HEIGHT - 40) / 10.0) * 10.0
            #if this special food is eaten the extra 3 points will be added to the score and increases the length of the snake by 5 blocks
            extra_points += 3
            Length_of_snake += 5

        
        CLOCK.tick(snake_speed_general)
        
    pygame.quit()
    quit()

main_menu()


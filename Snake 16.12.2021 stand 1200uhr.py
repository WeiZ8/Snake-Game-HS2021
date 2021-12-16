#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pygame is a programming language library in python with which games can be programed. So first of all we do import pygame. 
import pygame
from pygame import mixer
import pygame_menu

#We import the time module so that we can set the speed for the snake. 
import time

#We import the random module so that the food which the snake eats will appear at random locations on the display.
import sys, random

#Before we can do much with pygame, we  need to initialize it. This is done by pygame.init() which initializes all imported pygame modules. 
pygame.init()

#The color scheme used in Pygame is RGB i.e “Red Green Blue”. If we set all these to 0’s, the color will be black and all 255’s will be white. Here we have defined a view colors.

red = (175, 0, 42)
blue = (240, 248, 255)
darkblue = (61, 90, 110)
darkerblue = (0, 128, 0)
yellow = (255, 165, 0)
black = (0, 0, 0)


#Next we create the screen. For that we define the width and the height of the screen. 
dis_width = 800
dis_height = 600

#To create an actually screen with Pygame we make use of the display.set_mode() function. At the same time we use the above defined width and height. 
dis = pygame.display.set_mode((dis_width, dis_height))
#We want to give the pygame window the name "Snake Game". This is done by using the code below. 
pygame.display.set_caption('Snake Game')

#XXX 
clock = pygame.time.Clock()
 
#We define the size of the snake
snake_block = 10
#We define the speed of the snake
snake_speed_general = 30 



#we now choose and define the font
font_style = pygame.font.SysFont("comicsans", 25)
score_font = pygame.font.SysFont("comicsans", 25)
# As part of the fonts we also import our menu fonts (from pygame_menu)
font_menu = pygame_menu.font.FONT_8BIT

# Main_Menu
def main_menu():
   
    def start_the_game():
        gameLoop()
        # Do the job here !
        pass

    menu = pygame_menu.Menu(width=dis_width, height=dis_height, title='Welcome',
        theme=pygame_menu.themes.THEME_DARK);

    menu.add.text_input('Name : ', default='John Doe')
    menu.add.button('Play', start_the_game, font_name = font_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT, font_name = font_menu)
    menu.mainloop(dis)



 # End manu
def show_end_screen(game_score, display_width, display_height, replay, window):
  end_menu = pygame_menu.Menu(width=display_width, height=display_height, title='Game Over', 
theme=pygame_menu.themes.THEME_DARK);
  end_menu.add.label("Your Score: " + str(game_score), font_name = font_menu)
  end_menu.add.button("Replay Game", replay, font_name = font_menu)
  end_menu.add.button("Quit Game", pygame_menu.events.EXIT, font_name = font_menu)
  end_menu.mainloop(window)
       
 
#XXX 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, darkblue)
    dis.blit(value, [0, 0])
   
 
#Now we create the snake. It will be represented as a rectangle. To draw rectangles in Pygame, we  make use of the function called draw.rect() which will help us draw the rectangle with the desired color and size. 
#XXXmore explanation why we use for x in snake list and 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, darkerblue, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
    
#Samu part
def show_end_screen(game_score, display_width, display_height, replay, window):
  end_menu = pygame_menu.Menu(width=display_width, height=display_height, title='Game Over', 
theme=pygame_menu.themes.THEME_DARK);
  end_menu.add.label("Your Score:" + str(game_score))
  end_menu.add.button("Replay Game", replay)
  end_menu.add.button("Quit Game", pygame_menu.events.EXIT)
  end_menu.mainloop(window)    
 

def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2

# The variables x1_change and y1_change hold the updating values of the x and y coordinates.  
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    extra_points = 0

 
 #The snake game includes food for the snake. So the food needs to be first created. 
 #xxx more explanation needed
    foodx = round(random.randrange(40, dis_width - 40) / 10.0) * 10.0
    foody = round(random.randrange(40, dis_height - 40) / 10.0) * 10.0
    
 ##task1 from Deniz: obstacle needs to be defined
    obstaclex = round(random.randrange (40 , dis_width - 40) / 10.0) * 10.0
    obstacley = round(random.randrange(40, dis_height - 40) / 10.0) * 10.0

 #new: In our snake game we added some special food as well. It will pop up randomly, the snake has a few seconds to eat it and if eaten the snake will get faster. 
 #noch einfügen, dass special food nur ab und zu mal auftaucht. und nicht immer. 
    specialfoodx = round(random.randrange(40 , dis_width - 40) / 10.0) * 10.0
    specialfoody = round(random.randrange(40, dis_height - 40) / 10.0) * 10.0 

    while not game_over:
 
        while game_close == True:
            #the display screen is changed from the default black to blue using the fill() method.
            show_end_screen(str(Length_of_snake-1), dis_width, dis_height, gameLoop, dis)
           
            #We want to display the score of the player. To do this, we created the function “Your_score”. This function will display the length of the snake subtracted by 1 because that is the initial size of the snake.
            Your_score(Length_of_snake - 1 + extra_points)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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
        # When the user moves the snake by pressing the key we want the snake to move with the general speed defined with 15.            
        clock.tick(snake_speed_general)        

        #if players hits the boundaries of the screen, then they lose. The ‘if’ statement defines the limits for the x and y coordinates of the snake to be less than or equal to that of the screen.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        #the display screen is changed from the default black to blue using the fill() method.
        dis.fill(blue)
        pygame.draw.circle(dis, red, (foodx, foody), 6,6)
        ##task 2 from Deniz: obstacle need to be drawn
        pygame.draw.rect(dis, black, [obstaclex, obstacley, snake_block, snake_block])
        #new: this creates the special food. 
        pygame.draw.circle(dis, yellow, (specialfoodx, specialfoody), 6,6)
        snake_Head = []


        #The following code increases the size of the snake when it eats the food. The length of the snake is basically contained in a list and the initial size that is specified in the following code is one block.
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                #sound integration
                ding_Sound = mixer.Sound('Ding.mp3')
                ding_Sound.play()
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1 + extra_points)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            #sound integration
            ding_Sound = mixer.Sound('Ding.mp3')
            ding_Sound.play()
            foodx = round(random.randrange(40 , dis_width - 40) / 10.0) * 10.0
            foody = round(random.randrange(40 , dis_height - 40) / 10.0) * 10.0
            Length_of_snake += 1
            
  ##task 3 from Deniz: in case snake eats obstacle snake dies
        if x1 == obstaclex and y1 == obstacley:
            foodx = round(random.randrange(40 , dis_width - 40) / 10.0) * 10.0
            foody = round(random.randrange(40 , dis_height - 40) / 10.0) * 10.0
            game_close = True
 
  #new: the special food pops up on the display at random locations. 
        if x1 == specialfoodx and y1 == specialfoody:
            specialfoodx = round(random.randrange(40 , dis_width - 40) / 10.0) * 10.0
            specialfoody = round(random.randrange(40 , dis_height - 40) / 10.0) * 10.0
            #if this special food is eaten the extra 5 points will be added to the score
            extra_points += 3
            Length_of_snake += 5

        
        clock.tick(snake_speed_general)
        
    pygame.quit()
    quit()

main_menu()


# In[ ]:





import pygame
from pygame import mixer
import sys
import random
from pygame.math import Vector2
import time

# ---------[Game Settings]-----------
# The color scheme used in Pygame is RGB i.e “Red Green Blue”.
# If we set all these to 0’s, the color will be black and all 255’s will be white. Here we have defined a few colors.
BLACK = (0, 0, 0)
DARKBLUE = (61, 90, 110)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN1 = (25, 102, 25)
GREEN2 = (51, 204, 51)
GREEN3 = (233, 249, 185)
GREY1 = (105, 105, 105)
GREY2 = (169, 169, 169)
GREY3 = (211, 211, 211)
YELLOW = (250, 253, 15)

# Game control settings
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# -----------[SNAKE CLASS]--------------

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.color1 = GREEN1
        self.color2 = GREEN2
        self.score = 0
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * GRID_SIZE)
            y_pos = int(block.y * GRID_SIZE)
            block_rect = pygame.Rect((x_pos, y_pos), (GRID_SIZE, GRID_SIZE))
            #draw rect
            pygame.draw.rect(screen, self.color1, block_rect)
            pygame.draw.rect(screen, WHITE, block_rect, 1)

    #The head is moved to a new block. The block before the head gets the position where the head used to be.
    #Each block is moved to the previous block.
    def move_snake(self):
        if self.new_block == True:
            body_part = self.body[:]
            body_part.insert(0, body_part[0] + self.direction)
            self.body = body_part[:]
            self.new_block = False
        else:
            body_part = self.body[:-1]
            body_part.insert(0, body_part[0] + self.direction)
            self.body = body_part[:]

    def add_block(self):
        self.new_block = True
        game_over_sound.play()

    # Now we create the snake. It will be represented as a rectangle.
    # To draw rectangles in Pygame, we  make use of the function called draw.rect() which will help us draw the rectangle with the desired color and size.


# -----------[FOOD CLASS]--------------
class FOOD:
    def __init__(self):
        #create an x and y position
        self.randomize_position()
        self.color = RED

    def randomize_position(self):
        self.x = random.randint(0, GRID_NUMBER - 1)
        self.y = random.randint(0, GRID_NUMBER - 1)
        self.position = Vector2(self.x, self.y)

    # the food is created, colored and shaped
    def draw_food(self):
        #create a rectangle Rect(x, y, w, h)
        food_rect = pygame.Rect((int(self.position.x * GRID_SIZE) , int(self.position.y * GRID_SIZE)), (GRID_SIZE, GRID_SIZE))
        #draw rect(surface, color, rectangle)
        pygame.draw.rect(screen, self.color, food_rect)

class SPECIALFOOD:
    def __init__(self):
        self.color = YELLOW
        self.randomize_position()

    def randomize_position(self):
        self.x = random.randint(0, GRID_NUMBER - 1)
        self.y = random.randint(0, GRID_NUMBER - 1)
        self.position = Vector2(self.x, self.y)

    def draw_specialfood(self):
        # Rect(x, y, w, h)
        # create a rectangle Rect(x, y, w, h)
        specialfood_rect = pygame.Rect((int(self.position.x * GRID_SIZE), int(self.position.y * GRID_SIZE)),
                                (GRID_SIZE, GRID_SIZE))
        # draw rect(surface, color, rectangle)
        pygame.draw.rect(screen, self.color, specialfood_rect)

# -----------[MAIN GAME CLASS]-------------

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()
        self.specialfood = SPECIALFOOD()

    def update(self):
        self.snake.move_snake()
        self.check_fail()
        self.check_collision()

    def draw_elements(self):
        self.snake.draw_snake()
        self.food.draw_food()
        self.specialfood.draw_specialfood()
        self.draw_grid()

    def check_collision(self):
        #collision with food
        if self.snake.body[0] == self.food.position:
            #add another block to the snake
                self.snake.add_block()
                # reposition the food
                self.food.randomize_position()
                self.snake.pick_up_sound.play() #sound integration
        for block in self.food.position:
                if block == self.food.position:
                    self.food.randomize_position()
        # Check for collisions with normal special food
        if self.snake.body[0] == self.specialfood.position:
                self.snake.add_block()
                self.food.randomize_position()
                self.snake.pick_up_sound.play() # sound integration

    def check_fail(self):
        #check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < GRID_NUMBER or not 0 <= self.snake.body[0].y < GRID_NUMBER:
                self.game_over()
        # check if the head of the snake has collided with other parts of its body
        for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()

    def game_over(self):
        game_over_sound.play()
        pygame.quit()
        sys.exit()

    def draw_grid(self):
        #for row in range(cell_number)
        for y in range(GRID_NUMBER):
            # for col in range(cell_number)
            for x in range(GRID_NUMBER):
                if (x + y) % 2 == 0:
                    #Rect(x, y, w, h)
                    r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(screen, WHITE, r)
                else:
                    rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(screen, GREY3, rr)

    def draw_score(self):
        score_text = str(len(self.snake.positions) - 3)
        your_score = score_font.render(score_text, 1, DARKBLUE)
        screen.blit(your_score, (5, 10))

pygame.init() #initialize pygame
pygame.mixer.init()
#Add background music
pygame.mixer.music.load("Snake Game - Theme Song.mp3")
pygame.mixer.music.play(-1)

#Set sounds and music
pick_up_sound = pygame.mixer.Sound("Ding.mp3")
game_over_sound = pygame.mixer.Sound('game_over.mp3')

# display settings
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_NUMBER = 24
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
score_font = pygame.font.SysFont("comicsans", 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # To move the snake we will use key events from the KEYDOWN class of the Pygame library.
            # The K_UP, K_DOWN, K_LEFT, and K_RIGHT events will cause the snake to move up, down, left, and right, respectively.
                if event.type == SCREEN_UPDATE:
                    main_game.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if main_game.snake.direction.y != 1:
                            main_game.snake.direction = Vector2(UP)
                    if event.key == pygame.K_DOWN:
                        if main_game.snake.direction.y != -1:
                            main_game.snake.direction = Vector2(DOWN)
                    if event.key == pygame.K_LEFT:
                        if main_game.snake.direction.x != 1:
                            main_game.snake.direction = Vector2(LEFT)
                    if event.key == pygame.K_RIGHT:
                        if main_game.snake.direction.x != -1:
                            main_game.snake.direction = Vector2(RIGHT)
        screen.fill(WHITE)
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)


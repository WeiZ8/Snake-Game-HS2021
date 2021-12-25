#Snake Game

'''
Prequisites

The following packages and modules are REQUIRED to run the code:
*pygame
*time
*sys
*random
*typing

In case these packages are not installed yet, please run “pip install” for each package. 
If pip is not installed yet, please run "python get-pip.py" first.
*pip install pygame
*pip install random

For further information on the project, please refer to the "README.md" file. 

'''

#Import the necessary libraries
from typing import Text
import pygame, random, sys, time

# Initialize pygame and music
pygame.init()
pygame.mixer.init()
pick_up_sound = pygame.mixer.Sound("Ding.mp3")
game_over_sound = pygame.mixer.Sound('game_over.mp3')

# Global Variables
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 20  # 20 pixels allows us to get 24 grid squares across 25 grid squares down
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("comicsans", 30)
pygame.display.set_caption('Snake Game')

FPS = 10  # 10ticks per second

# Snake will always start in the center
CENTER = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

# The color scheme used in Pygame is RGB i.e “Red Green Blue”.
# Here we have defined a few colors.
BLACK = (0, 0, 0)
DARKBLUE = (61, 90, 110)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (25, 102, 25)
GREY1 = (105, 105, 105)
GREY2 = (211, 211, 211)
YELLOW = (250, 253, 15)

# Declare directions / control settings - xy tuples
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# ---------------------[MENU]------------------------
# We now create a small function to help us expedite the process of writing text for the menus
# We can get the dimensions of the rendered text image using text.get_rect(), which returns a Rect object with width and height attributes, to center the text respective to the window

def center_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(SCREEN_WIDTH / 2, y))
    surface.blit(textobj, textrect)

def button_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# We create the starting menu
def main_menu():
    while True:
        
        screen.fill(BLACK)
        center_text('Main Menu', font, WHITE, screen, 40, 40)
        
        mx, my = pygame.mouse.get_pos()

        # Creating the buttons
        # We use the virtual property of rect and assign its center to the middle of the screen, define its size and color

        button_1 = pygame.Rect(0, 0, 200, 75)
        button_1.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        pygame.draw.rect(screen, WHITE, button_1)

        button_2 = pygame.Rect(0, 0, 200, 75)
        button_2.centerx = ((SCREEN_WIDTH / 2))
        button_2.centery = ((button_1.centery) + button_1.height * 1.5)  # We distanciate the second button by the lenght of exaclty 0.5 button

        pygame.draw.rect(screen, RED, button_1)
        pygame.draw.rect(screen, RED, button_2)


        # Adding text to the buttons
        # We use True in "font_style.render", to activate antialiasing and make the text smoother
        Text_button_1 = font.render("Play", True, 20)
        text_rect_1 = Text_button_1.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(Text_button_1, text_rect_1)

        Text_button_2 = font.render("Instructions", True, 20)
        text_rect_2 = Text_button_2.get_rect(center=(SCREEN_WIDTH / 2, button_2.centery))
        screen.blit(Text_button_2, text_rect_2)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if button_1.collidepoint((mx, my)):
                if click:
                    run()
            if button_2.collidepoint((mx, my)):
                if click:
                    options()

        pygame.display.update()
        clock.tick(60)

def options():
    running = True
    while running:
        screen.fill(BLACK)
        mx, my = pygame.mouse.get_pos()
        # Text for options menu (within the instruction button)
        Title = center_text('Options', font, WHITE, screen, 40, 40)
        Info_1 = center_text('Eat fruit to get longer', font, WHITE, screen, SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT - 30 * 12)
        Info_2 = center_text('One point', font, WHITE, screen, SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT - 30 * 10)
        Info_3 = center_text('Five points', font, WHITE, screen, SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT - 30 * 8)

        # Images/symbols of the food items next to the desciption
        normal_food_sym = pygame.Rect(0, 0, 25, 25)
        normal_food_sym.midleft = 100, SCREEN_HEIGHT - 30 * 10
        pygame.draw.rect(screen, RED, normal_food_sym, 40, 10)

        special_food_sym = pygame.Rect(0, 0, 25, 25)
        special_food_sym.midleft = 100, SCREEN_HEIGHT - 30 * 8
        pygame.draw.rect(screen, YELLOW, special_food_sym, 40, 10)

        # Back button
        Back_button = pygame.Rect(0, 0, 150, 50)
        Back_button.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30 * 2)
        pygame.draw.rect(screen, (GREY1), Back_button)

        Back_button_text = font.render("Back", True, 10)
        Back_button_text_rect = Back_button_text.get_rect(center=(Back_button.center))
        screen.blit(Back_button_text, Back_button_text_rect)

        if Back_button.collidepoint((mx, my)):
            if click:
                main_menu()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

# -----------[SNAKE CLASS]--------------
# Within the snake class, we define all features and settings of the snake
# Attributes of the snake incl. length, position of the snake, possible directions when key pressed, its color and the starting score
class Snake:
    def __init__(self):
        self.length = 3
        self.score = 0
        self.positions = [CENTER]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.outline_color = WHITE

    # define the head position
    def get_head_position(self):
        return self.positions[0]  # the very first position of our array

    # the direction that it gets passed to the turn function
    # we are taking the x * -1 and y*-1 which gives us the reversed direction we are heading
    def turn(self, new_dir):
        if self.length > 1 and (new_dir[0] * -1, new_dir[1] * -1) == self.direction:
            return
        else:
            self.direction = new_dir

    # move function for the snake
    def move(self):
        scored = self.score
        
        # decomposition of the tuples
        cur = self.get_head_position()
        x, y = self.direction
        new_pos = ((cur[0] + (x * GRID_SIZE)), cur[1] + (y * GRID_SIZE))
        # collision with wall/boundaries
        if new_pos[0] < 0 or new_pos[0] >= SCREEN_WIDTH or new_pos[1] < 0 or new_pos[1] >= SCREEN_HEIGHT:
            game_over(scored)
            game_over_sound.play()
        elif len(self.positions) > 2 and new_pos in self.positions[2:]:
            game_over(scored)
            game_over_sound.play()
        else:
            self.positions.insert(0, new_pos)
            if len(self.positions) > self.length:
                self.positions.pop()

    # Now we create the snake. It will be represented as a rectangle.
    # To draw rectangles in Pygame, we  make use of the function called draw.rect() which will help us draw the rectangle
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, self.outline_color, r, 1)

# -----------[FOOD CLASS]--------------
# Within the food class, we define all features and settings of the standard food 
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    # define the random position of the food
    def randomize_position(self):
        rand_x = random.randint(0, int(GRID_WIDTH - 1))
        rand_y = random.randint(0, int(GRID_HEIGHT - 1))
        self.position = (rand_x * GRID_SIZE, rand_y * GRID_SIZE)

    # the food is created, colored and shaped
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r, 40, 10)

# We define all features and settings of the special food       
class Specialfood():
    def __init__(self):
        self.position = (0, 0)
        self.color = YELLOW
        self.randomize_position()

    # define the random position of the spcial food    
    def randomize_position(self):
        rand_x = (random.randint(0, int(GRID_WIDTH) - 1))
        rand_y = (random.randint(0, int(GRID_HEIGHT) - 1))
        self.position = (rand_x * GRID_SIZE, rand_y * GRID_SIZE)

    # the special food is created, colored and shaped    
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, (r), 40, 10)

# --------------[GAME WORLD CLASS]--------------
# Reposition of the snake and the food of the world
# Also the logic to the key presses of the game
class World:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.specialfood = Specialfood()

    def update(self):
        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1  #increase length of snake by 1 when eating the standard food
            self.snake.score += 1  #increase score of the game by 1 when eating the standard food
            self.food.randomize_position()
            pick_up_sound.play()  # sound effect when snake picks up food

        if self.snake.get_head_position() == self.specialfood.position:
            self.snake.length += 3  #increase length of snake by 1 when eating the special food
            self.snake.score += 5  #increase score of the game by 5 when eating the special food
            self.specialfood.randomize_position()
            pick_up_sound.play()  # sound effect when snake picks up food

    def draw(self, surface):
        self.snake.draw(surface)
        self.food.draw(surface)
        self.specialfood.draw(surface)

    def score(self):
        return self.snake.score

    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            # To move the snake we will use key events from the KEYDOWN class of the Pygame library.
            # The K_UP, K_DOWN, K_LEFT, and K_RIGHT events will cause the snake to move up, down, left, and right, respectively
            if event.key == pygame.K_UP:
                self.snake.turn(UP)
            elif event.key == pygame.K_DOWN:
                self.snake.turn(DOWN)
            elif event.key == pygame.K_LEFT:
                self.snake.turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                self.snake.turn(RIGHT)

def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):  # we always want to pass on an integer in a range
        # create a nested for loop
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:  # even square positions
                # define two tuples inside the rect
                r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                # draw the rectangles
                pygame.draw.rect(surface, WHITE, r)
            else:
                rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, GREY2, rr)

def run():
    # define a surface to draw on
    # creates a surface exactly the same size as the display area
    surface = pygame.Surface(screen.get_size())
    # convert the screen to run in the resolution of the monitor
    surface = surface.convert()

    draw_grid(surface)

    world = World()

    font = pygame.font.SysFont("comicsans", 30)
    # Add background music
    pygame.mixer.music.load("Snake Game - Theme Song.mp3")
    pygame.mixer.music.play(-1)

    # Creating the game loop
    running = True
    while running:
        # Checking all the events that are happening on our screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    world.handle_keys(event)

        clock.tick(FPS)
        world.update()

        draw_grid(surface)
        world.draw(surface)

        screen.blit(surface, (0, 0))
        scored = world.score()
        text = font.render("Your Score: {0}".format(scored), 1, DARKBLUE)
        screen.blit(text, (5, 10))
        pygame.display.update()
        
#----GAME OVER----
#game over scene, this takes the score to display as the argument
def game_over(scored):
    game_over_sound.play()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)

        #showing 'You lost' in red color
        game_over_message = font.render('You Lost' , True , RED)
        #showing 'You score was SCORE'
        game_over_score = font.render(f'Your Score was {scored}', True , WHITE)

        font_pos_message = game_over_message.get_rect(center=(CENTER))
        font_pos_score = game_over_score.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+40))
        screen.blit(game_over_message , font_pos_message)
        screen.blit(game_over_score , font_pos_score)
        pygame.display.update()
          
        #here what we are doing is we use time.sleep() to stop our program for 3 seconds ,after 3 seconds, we call our main_menu()
        time.sleep(3)
        main_menu()

main_menu()

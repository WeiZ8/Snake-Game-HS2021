from typing import Text
import pygame
import sys
import random

# Initialize pygame
pygame.init()

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

# Fonts
font_style = pygame.font.SysFont("comicsans", 30)
#Add background music
pygame.mixer.music.load("Snake Game - Theme Song.mp3")
pygame.mixer.music.play(-1)

# display settings
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Global settings
clock = pygame.time.Clock()
#Set sounds and music
pick_up_sound = pygame.mixer.Sound("Ding.mp3")

# Game control settings
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# -----------[SNAKE CLASS]--------------

class Snake():
    def __init__(self):
        self.length = 3
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color1 = GREEN1
        self.color2 = GREEN2
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 3
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    # Now we create the snake. It will be represented as a rectangle.
    # To draw rectangles in Pygame, we  make use of the function called draw.rect() which will help us draw the rectangle with the desired color and size.
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color1, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # To move the snake we will use key events from the KEYDOWN class of the Pygame library.
            # The K_UP, K_DOWN, K_LEFT, and K_RIGHT events will cause the snake to move up, down, left, and right, respectively.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


# -----------[FOOD CLASS]--------------
class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    # the food is created, colored and shaped
    def draw_Food(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)

class Specialfood():
    def __init__(self):
        self.position = (0, 0)
        self.color = YELLOW
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw_Specialfood(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, WHITE, r)
            else:
                rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, GREY3, rr)

# -----------[MAIN GAME CLASS]--------------
def main():
    pygame.init()
    # Initialise game window
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()
    specialfood = Specialfood()

    score_font = pygame.font.SysFont("comicsans", 30)

    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        # Check for collisions with normal food
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            pick_up_sound.play() #sound integration
            food.randomize_position()
        # Check for collisions with normal special food
        if snake.get_head_position() == specialfood.position:
            snake.length += 2
            snake.score += 5
            pick_up_sound.play() #sound integration
            specialfood.randomize_position()

        snake.draw(surface)
        food.draw_Food(surface)
        specialfood.draw_Specialfood(surface)
        screen.blit(surface, (0, 0))
        # We are adding a starting score
        your_score = score_font.render("Your Score: {0}".format(snake.score), 1, DARKBLUE)
        screen.blit(your_score, (5, 10))
        pygame.display.update()


# We now create a small function to help us expedite the process of writing text for the menus
# We can get the dimensions of the rendered text image using text.get_rect(), which returns a Rect object with width and height attributes, to center the text respective to the window

def center_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(SCREEN_WIDTH / 2, y))
    surface.blit(textobj, textrect)


def left_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def button_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# ---------------------[MENU]------------------------
# neww
def main_menu():
    while True:

        screen.fill((0, 0, 0))
        center_text('Main menu', font_style, (255, 255, 255), screen, 40, 40)

        mx, my = pygame.mouse.get_pos()

        # Creating the buttons
        # We use the virtual property of rect and assign its center to the middle of the screen

        button_1 = pygame.Rect(0, 0, 200, 75)
        button_1.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        pygame.draw.rect(screen, (255, 255, 255), button_1)

        button_2 = pygame.Rect(0, 0, 200, 75)
        button_2.centerx = ((SCREEN_WIDTH / 2))
        button_2.centery = ((
                                button_1.centery) + button_1.height * 1.5)  # We distanciate the second button by the lenght of exaclty 0.5 button

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        if button_1.collidepoint((mx, my)):
            if click:
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        # Adding text to the buttons
        # We use True in "font_style.render", to activate antialiasing and make the text smoother
        Text_button_1 = font_style.render("Play", True, 20)
        text_rect_1 = Text_button_1.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(Text_button_1, text_rect_1)

        Text_button_2 = font_style.render("Instructions", True, 20)
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

        pygame.display.update()
        clock.tick(30)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        # Text for options menu
        Title = center_text('Options', font_style, (255, 255, 255), screen, 20, 20)
        Info_1 = center_text('Eat fruit to get longer', font_style, (255, 255, 255), screen, SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT - 30 * 12)
        Info_2 = center_text('One point', font_style, (255, 255, 255), screen, SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT - 30 * 10)
        Info_3 = center_text('Five points', font_style, (255, 255, 255), screen, SCREEN_WIDTH / 2,
                             SCREEN_HEIGHT - 30 * 8)

        # Images/symbols describing the text

        normal_food_sym = pygame.Rect(0, 0, 25, 25)
        normal_food_sym.midleft = 100, SCREEN_HEIGHT - 30 * 10
        pygame.draw.rect(screen, RED, normal_food_sym)

        special_food_sym = pygame.Rect(0, 0, 25, 25)
        special_food_sym.midleft = 100, SCREEN_HEIGHT - 30 * 8
        pygame.draw.rect(screen, YELLOW, special_food_sym)

        # Back button
        Back_button = pygame.Rect(0, 0, 150, 50)
        Back_button.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30 * 2)
        pygame.draw.rect(screen, (GREY1), Back_button)

        Back_button_text = font_style.render("Back", True, 10)
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
        clock.tick(30)


main_menu()


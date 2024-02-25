# importing modules
import pygame
import random
import sys
import time

# importing sub-modules
from random import randint

# initializing modules
pygame.init()
pygame.mixer.init()
pygame.font.init()

# game settings
# game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Duel"

FPS = 60

# rgb color tuples
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 162, 232)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

YELLOW = (255, 255, 0)
PURPLE = (150, 0, 150)

ALPHA = GREEN

# game constants
PLAYER_SPEER = 8
BULLET_SPEED = 15

LINE_TICKNESS = 2

# game variables
# settings varaibles
__version__ = "v1.0"
running = True

p1_health = 50
p2_health = 50

p1_bullet_active = True
p2_bullet_active = True

image_show = True

# setting up screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TITLE = pygame.display.set_caption(f"{SCREEN_TITLE} {__version__}")
MOUSE_VISIBILITY = pygame.mouse.set_visible(True)
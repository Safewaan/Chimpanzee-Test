# Imports
import pygame
from pygame.locals import *

# Images
numList = []
for x in range(5):
    numList.append(pygame.image.load(str(x + 1) + ".png"))

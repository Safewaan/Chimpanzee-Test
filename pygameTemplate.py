# Imports
import sys
import pygame
import random
from pygame.locals import *

# Local Imports
import NumberImages
import CordGenerator
from PygameColours import *

# Pygame init
pygame.init()

# FPS
fps = 60
fpsClock = pygame.time.Clock()

# Screen settings
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption ('Monky Together sTRonk')
screen.fill(colourLightCyan)

# Grid variables
gD = 30
incrementX, incrementY = width / gD, height / gD
incrementXTotal, incrementYTotal = 0, 0

# Image loader
numList = NumberImages.imageList(gD) # Images list
cordsList = CordGenerator.CordGen(gD, width, height) # Coordinates list

for x in range(len(numList)):
    imageResizer = pygame.transform.smoothscale(numList[x], (int(incrementX), int(incrementY)))
    screen.blit(imageResizer, (cordsList.pop(random.randint(0, len(cordsList) - 1))))

# Generates lines
for xy in range (gD - 1):
  # x-axis
  incrementXTotal += incrementX
  pygame.draw.line(screen, colourBlack, [incrementXTotal, 0], [incrementXTotal, height], 1)
  
  # y-axis
  incrementYTotal += incrementY
  pygame.draw.line(screen, colourBlack, [0, incrementYTotal], [width, incrementYTotal], 1)

# Game loop.
while True:

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Update.

  # Draw.

  pygame.display.flip()
  fpsClock.tick(fps)

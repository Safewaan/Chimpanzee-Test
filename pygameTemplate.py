# Imports
import sys
import pygame
import random
import CordGenerator
from pygame.locals import *
from PygameColours import *
from NumberImages import *

# Pygame init
pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

# Screen settings
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption ('Monky Together sTRonk')
screen.fill(colourLightCyan)

# Grid variables
gD = 5
incrementX, incrementY = width / gD, height / gD
incrementXTotal, incrementYTotal = 0, 0

# Number images
cordsList = CordGenerator.CordGen(gD, width, height)

for x in range(len(numList)):
  imageLoader = numList[x].get_rect()
  imageLoader = imageLoader.move(cordsList.pop(random.randint(0, len(cordsList) - 1)))
  screen.blit(numList[x], imageLoader)

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

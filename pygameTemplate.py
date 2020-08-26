#Imports
import sys
import pygame
import random
import CordGenerator
from pygame.locals import *
from PygameColours import *
from NumberImages import *

#Pygame init
pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

#Screen settings
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption ('Monky Together sTRonk')
screen.fill(colourLightCyan)

gD = 5
incrementX, incrementY = width / gD, height / gD
incrementXTotal, incrementYTotal = 0, 0

#Number Images
cordsList = CordGenerator.CordGen(gD, width, height)

one_rect = one.get_rect()
one_rect = one_rect.move(cordsList.pop(random.randint(0, len(cordsList))))
screen.blit(one, one_rect)

"""
two_rect = two.get_rect()
two_rect = two_rect.move(CordGenerator.CordGen(gD, width, height).pop(random.randint(0, len(CordGenerator.CordGen(gD, width, height)))))
screen.blit(two, two_rect)

three_rect = three.get_rect()
three_rect = three_rect.move(CordGenerator.CordGen(gD, width, height).pop(random.randint(0, len(CordGenerator.CordGen(gD, width, height)))))
screen.blit(three, three_rect)
"""

#Generates lines

for xy in range (gD - 1):
  #x-axis
  incrementXTotal += incrementX
  pygame.draw.line(screen, colourBlack, [incrementXTotal, 0], [incrementXTotal, height], 1)
  
  #y-axis
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

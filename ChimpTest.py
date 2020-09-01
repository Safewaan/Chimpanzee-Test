# Imports
import sys
import pygame
import random
import os
from pygame.locals import *

# Local Imports
import NumberImages
import CordGenerator
import LineGenerator
from PygameColours import *
from TestVariables import *

# Pygame init
pygame.init()

# FPS
fps = 60
fpsClock = pygame.time.Clock()

# Screen settings
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption ('Monky Together sTRonk')
screen.fill(colourLightCyan)

# Grid variables
incrementX, incrementY = int(width / gD), int(height / gD)

# Variables
currentNum = 0
white = pygame.image.load(os.path.join("sprites", "white.png"))
white = pygame.transform.smoothscale(white, (incrementX, incrementY))

# Image loader
numList = NumberImages.imageList(gD) # Images list
cordsList = CordGenerator.cordGen(gD, width, height) # Coordinates list
imageRectList = [] #Image rectangles list

for x in range(len(numList)):
  image = pygame.transform.smoothscale(numList[x], (incrementX, incrementY))
  imageRect = image.get_rect()
  imageRect = imageRect.move((cordsList.pop(random.randint(0, len(cordsList) - 1))))
  imageRectList.append(imageRect)
  screen.blit(image, imageRectList[x])

# Generates lines
LineGenerator.lineGen(gD, incrementX, incrementY)

# Game loop.
while True:

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == MOUSEBUTTONDOWN:
      mouse_pos = event.pos
      
      if imageRectList[currentNum].collidepoint(mouse_pos):
        
        if currentNum == 0:
          for x in range(len(numList)):
            screen.blit(white, imageRectList[x])
          LineGenerator.lineGen(gD, incrementX, incrementY)
        
        currentNum += 1

      else:
        pygame.quit()
        sys.exit()

  # Update.

  # Draw.

  pygame.display.flip()
  fpsClock.tick(fps)
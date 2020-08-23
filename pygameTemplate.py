#Imports
import sys
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
#Colours
colourRed = pygame.Color(255,0,0)
colourBlue = pygame.Color(0,0,255)
colourGreen = pygame.Color(0,255,0)
colourBlack = pygame.Color(0,0,0)
colourWhite = pygame.Color(255,255,255)
colourOrange = pygame.Color(255,128,0)
colourBrown = pygame.Color(204,102,0)

#Screen settings
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption ('Monky Together sTRonk')
screen.fill(colourWhite)

# Game loop.
while True:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  
  # Draw.
  gD = 6
  incrementX, incrementY = width / gD, height / gD
  incrementXTotal, incrementYTotal = 0, 0
    
  #Generates lines on the x-axis
  for x in range (gD - 1):
      incrementXTotal += incrementX
      pygame.draw.line(screen, colourBlack, [incrementXTotal, 0], [incrementXTotal, height], 5)

  #Generates lines on the y-axis
  for y in range (gD - 1):
    incrementYTotal += incrementY
    pygame.draw.line(screen, colourBlack, [0, incrementYTotal], [width, incrementYTotal], 5)
      
  pygame.display.flip()
  fpsClock.tick(fps)
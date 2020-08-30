# Imports
import pygame
from pygame.locals import *

# Local imports
from PygameColours import *
from TestVariables import *

def lineGen(gD, incrementX, incrementY):
    """
    Generates lines that create perfect squares in any given resolution.

    Paramaters:
    gD: int
        The dimensions of the grid.
    
    incrementX: int
        Increments of the x resolution divided by gD.

    incrementY: int
        Increments of the y resolution divided by gD.
        
    Returns:
    none.

    """
    
    # Variables
    incrementXTotal, incrementYTotal = 0, 0

    # Main loop
    for xy in range (gD - 1):
        # x-axis
        incrementXTotal += incrementX
        pygame.draw.line(screen, colourBlack, [incrementXTotal, 0], [incrementXTotal, height], 1)
    
        # y-axis
        incrementYTotal += incrementY
        pygame.draw.line(screen, colourBlack, [0, incrementYTotal], [width, incrementYTotal], 1)
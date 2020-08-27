# Imports
import pygame
import CordGenerator
from pygame.locals import *

# Images
def imageList(gD):
    """
    Generates list of all pygame.image.load to be called in a loop. 

    Paramaters:
    gD: int
        The dimensions of the grid.

    Returns:
    numList: list
        List of all pygame.image.load lines.
    """
    
    # Variables
    numList = []

    # Prevents ctd if gD ** 2 is larger than available images
    if gD ** 2 >= 20:
        loopNum = 19
    
    else: 
        loopNum = gD ** 2

    # Main loop
    for x in range(loopNum):
        numList.append(pygame.image.load(str(x + 1) + ".png"))

    # Return
    return numList
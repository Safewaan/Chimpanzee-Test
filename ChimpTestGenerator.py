#Imports
import random

def ChimpTestGen(gD, n):
    """
    Generates a grid with dimensions gD ** 2 with integers ranging from zero to n in random positions within the grid.

    Paramaters:
    gD: int
        The dimensions of the grid.

    n: list
        A list with integers zero to n. Also includes asterisks to fill in missing spots.

    Returns:
    (none yet)
    """

    #Appends asterisks to list n to fill in missing spots within the grid
    for c in range(gD ** 2 - len(n)):
        n.append("*")

    random.shuffle(n)

    #Generates grids with values
    for x in range(gD):
        for y in range(gD):
            if y == gD - 1:
                print (str(n.pop(0)) + " ")
            else:
                print (str(n.pop(0)) + " ", end = "")

ChimpTestGen(int(input()), list(range(int(input()))))

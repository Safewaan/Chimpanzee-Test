def CordGen(gD, width, height):
    """
    Generates coordinates of all line intersections. 

    Paramaters:
    gD: int
        The dimensions of the grid.

    width: int
        Width of the pygame.

    height: int
        Height of the pygame.
    Returns:
    cords: list
        List of all coordinates.
    """

    #Variables
    incrementX, incrementY = width / gD, height / gD
    incrementXTotal, incrementYTotal = 0, 0

    cords = []

    #Main loop
    for y in range(gD):
        for x in range(gD):
            cords.append([incrementXTotal, incrementYTotal])
            incrementXTotal += incrementX
            
        incrementYTotal += incrementY
        incrementXTotal = 0

    #Return
    return (cords)

print (CordGen(5, 800, 800))
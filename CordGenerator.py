def CordGen(gD, width, height):
    
    incrementX, incrementY = width / gD, height / gD
    incrementXTotal, incrementYTotal = 0, 0

    cords = []

    for y in range(gD - 1):
        incrementYTotal += incrementY
        for x in range(gD - 1):
            incrementXTotal += incrementX
            cords.append([incrementXTotal, incrementYTotal])

        incrementXTotal = 0

    print (cords)

CordGen(5, 800, 800)


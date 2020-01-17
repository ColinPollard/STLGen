import numpy as np
import noise

def PerlinHash(array, minValue, maxValue, maxX, maxY, maxZ):
    maxAltitude = 16
    surfaceValues = np.zeros((maxX,maxY))
    zOffset = int(maxZ/4)
    thickness = 3

    octaves = 3
    persistence = .2
    lacunarity = 2

    for i in range(1, maxX-1):
        for j in range(1, maxY-1):
            surfaceValues[i][j] = noise.pnoise2(i / maxAltitude,
                                        j / maxAltitude,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=maxX,
                                        repeaty=maxY,
                                        base=0)

    # Take 2d surface and map the brightness values to z values in 3d array
    for i in range (1, maxX):
        for j in range (1, maxY):
            # Iterate downward from selected value by thickness
            for z in range (int(maxAltitude * surfaceValues[i][j]) + zOffset-thickness, int(maxAltitude * surfaceValues[i][j]) + zOffset):
                if z < 1:
                    continue
                array[i,j,z] = 16

    return array
from random import randint
import numpy as np

# Creates a new zero indexed array with size xyz
# Makes an empty array one size larger in each dimension to account for closing the shape
def CreatePoints(x,y,z):
    return np.zeros((z+1,y+1,x+1))

# Iterate through point array and set each point to a random value
def PureRandomHash(array, minValue, maxValue, maxX, maxY, maxZ):
    for index in np.nditer(array, op_flags = ['readwrite']):
        index[...] = randint(minValue, maxValue)
    return array

def HorizontalDeltaHash(array, minValue, maxValue, maxX, maxY, maxZ):
    array[1,1,1] = randint(minValue, maxValue)
    previousPoint = (1,1,1)

    for z in range (1, maxZ - 1):
        for y in range(1, maxY - 1):
            for x in range(1, maxX - 1):
                # Set current point to previous point's value with a random factor
                array[x, y, z] = array[previousPoint] + randint(-(maxValue-minValue)/4, (maxValue-minValue)/4)

                # If the value is out of bounds, set to min/max
                if array[x, y, z] > maxValue:
                    array[x, y, z] = maxValue

                elif array[x, y, z] < minValue:
                    array[x, y, z] = minValue

                previousPoint = (x, y, z)
    return array

def VerticalDeltaHash(array, minValue, maxValue, maxX, maxY, maxZ):
    array[1,1,1] = randint(minValue, maxValue)
    previousPoint = (1,1,1)

    for x in range (1, maxX - 1):
        for y in range(1, maxY - 1):
            for z in range(1, maxZ - 1):
                # Set current point to previous point's value with a random factor
                array[x, y, z] = array[previousPoint] + randint(-(maxValue-minValue)/4, (maxValue-minValue)/4)

                # If the value is out of bounds, set to min/max
                if array[x, y, z] > maxValue:
                    array[x, y, z] = maxValue

                elif array[x, y, z] < minValue:
                    array[x, y, z] = minValue

                previousPoint = (x, y, z)
    return array

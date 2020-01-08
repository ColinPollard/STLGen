from random import randint
import numpy as np

#Creates a new zero indexed array with size xyz
def CreatePoints(x,y,z):
    return np.zeros((z,y,x))

#Iterate through point array and set each point to a random value
def RandomHash(array, minValue, maxValue):
    for index in np.nditer(array, op_flags = ['readwrite']):
        index[...] = randint(minValue, maxValue)
    return array

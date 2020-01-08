import numpy as np
from matplotlib import pyplot
from mpl_toolkits import mplot3d
from stl import mesh

from Waves.MarchingCubes import GenerateSingleCubeMesh
from Waves.SpaceGeneration import CreatePoints, RandomHash

points = np.array([\
[-1, -1, -1],
[+1, -1, -1],
[+1, +1, -1],
[-1, +1, -1],
[-1, -1, +1],
[+1, -1, +1],
[+1, +1, +1],
[-1, +1, +1]])

faces = np.array([
[0,3,1],
[1,3,2],
[0,4,7],
[0,7,3],
[4,5,6],
[4,6,7],
[5,1,2],
[5,2,6],
[2,3,6],
[3,7,6],
[0,1,5],
[0,5,4]])


emptyArray = CreatePoints(2,2,2)
randomPoints = RandomHash(emptyArray, 0, 16)

newPoints, newFaces = GenerateSingleCubeMesh(randomPoints, 8, 2, 2, 2)



cube = mesh.Mesh(np.zeros(newFaces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(newFaces):
    for j in range(3):
        cube.vectors[i][j] = newPoints[f[j],:]

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(cube.vectors))

# Auto scale to the mesh size
scale = cube.points.flatten('F')
axes.auto_scale_xyz(scale, scale, scale)
# Show the plot to the screen
pyplot.show()

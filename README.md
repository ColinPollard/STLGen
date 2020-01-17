# STLGen
#### Creates STL meshes from point cloud distributions using the marching cubes technique.

---
### Data Flow
* Empty 3D space of points is created as a shape (x,y,z) numpy array.
* A hashing function is used to generate "surface" values for each 3D point in space. (x,y,z) => s 
* The CubeRenderer then creates a surface using each point above the surface level using the marching cubes technique. 
* The mesh is then constructed from the CubeRenderer, displayed and saved.

---
### Files and Features
##### Test.py
Has basic test for creating a mesh using the framework, displaying in a 3d viewer, and saving the file. Calls methods in PointGeneration or TerrainGen to create point cloud, and then uses CubeRender to create the point and face arrays. Finally, numpy-stl is used to turn the point and face arrays into a mesh, and is drawn using matplotlib.

##### PointGeneration.py & TerrainGen.py
These files contain hashing methods and helper methods to create point clouds from scratch. PointGeneration.py contains basic hashes using the built in random number generation, including the vertical and horizontal generations as shown below. TerrainGen.py contains perlin noise based hashes to create more terrain-like point clouds.

##### CubeRender.py
Accepts a point cloud with dimensions, and uses marching cubes to generate two new arrays from it. Returns points and faces, representing 3d points, and sets of indexes of those points.

---
### Dependencies and Acknowledgements
Requires numpy, numpy-stl (must be installed manually, as the default is the wrong stl library), matplotlib, noise, and mpl_toolkits.

Inspiration from Sebastian Lague's Coding Adventure.

---
### Images
![HorizontalHash Generation](https://github.com/ColinPollard/STLGen/blob/master/ProcessedData/HorizontalHash%20Example.PNG)
HorizontalHash Generation (PointGeneration.py)

![PerlinHash Generation](https://github.com/ColinPollard/STLGen/blob/master/ProcessedData/PerlinHash%20Example.PNG)
PerlinHash Generation (TerrainGen.py)

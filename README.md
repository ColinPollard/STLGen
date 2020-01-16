# STLGen
A project implementing the marching cubes algorithm to create an stl mesh from a point cloud distribution. 
This program first creates an empty 3D space of points, and then uses a hashing function to generate "surface" values for each 3D point in space. The CubeRenderer then creates a surface using each point above the surface level using the marching cubes technique. In the example test file, the surface is saved locally, and then displayed using the built in stl viewer.
Requires numpy, numpy-stl (must be installed manually, as the default is the wrong stl library), matplotlib, and mpl_toolkits.
Inspiration from Sebastian Lague's Coding Adventure.
![HorizontalHash Generation](https://github.com/ColinPollard/STLGen/blob/master/ProcessedData/HorizontalHash%20Example.PNG)

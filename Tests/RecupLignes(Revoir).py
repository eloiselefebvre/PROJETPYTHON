

import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

import Principal

file = open('/Users/eloiselefebvre/Desktop/Projet 2e année/V_HULL_Normals_Outward.STL','r')
counter = 0
ListeFacette = []


Principal.listefile(file,ListeFacette,counter)

file.close()




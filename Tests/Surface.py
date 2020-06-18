import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

import Principal
Mat_PointA = np.array([[0,2,3],[1,2,3]])
Mat_PointB = np.array([[0,2,3],[1,2,3]])
Mat_PointC = np.array([[0,2,3],[1,2,3]])
NbFacettes = 3
Liste_Surface = []

Principal.surface(Mat_PointA,Mat_PointB,Mat_PointC,NbFacettes,Liste_Surface)


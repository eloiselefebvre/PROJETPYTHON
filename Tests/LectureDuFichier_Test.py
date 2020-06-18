import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

import Principal
print("fin de l'import du principal")


counter = 0
ListeFacette = []
New_Liste = []
Mat_Normales = np.array([0,0,0])
Mat_PointA = np.array([0,0,0])
Mat_PointB = np.array([0,0,0])
Mat_PointC = np.array([0,0,0])
Liste_Surface = []
NbFacettes = 0


print("Début de récupération des données >>>>>>")


file = open('/Users/eloiselefebvre/Desktop/Projet 2e année/STL_Test.stl','r')
file.readline()





print("test de surface : ")

Principal.lecturefichier(Mat_PointA,Mat_PointB,Mat_PointC,Mat_Normales,file)

print("fin du test")

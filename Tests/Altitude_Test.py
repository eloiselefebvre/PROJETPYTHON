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
Liste_Altitude = []


print("Début de récupération des données >>>>>>")


file = open('/Users/eloiselefebvre/Desktop/Projet 2e année/STL_Test.stl','r')
file.readline()



Mat_PointA,Mat_PointB,Mat_PointC,Mat_Normales,NbFacettes = Principal.lecturefichier(Mat_PointA,Mat_PointB,Mat_PointC,Mat_Normales,file)
Liste_Surface = Principal.surface(Mat_PointA,Mat_PointB,Mat_PointC,NbFacettes,Liste_Surface)


print("test d'altitude : ")

Principal.altitude(Mat_PointA,Mat_PointB,Mat_PointC,Liste_Altitude)

print("fin du test")


import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot




#OUVERTURE ET LECTURE DU FICHIER STL
file = open('/Users/eloiselefebvre/Desktop/Projet 2e année/V_HULL_Normals_Outward.STL','r')
file.readline()



#>>
#CREATION DES VARIABLES ET DES STRUCTURES DE DONNEES
New_Liste = []
ListeFacette = []
Mat_Normales = np.array([0,0,0])
Mat_PointA = np.array([0,0,0])
Mat_PointB = np.array([0,0,0])
Mat_PointC = np.array([0,0,0])
Liste_Surface = []
Liste_Altitude = []
Liste_Normale = []
Liste_N_Normale = []
Liste_Force_FaXn = []
Liste_Force_FaYn = []
Liste_Force_FaZn = []
Liste_Fa = []
Liste_Zg=[]
gravity = 9.81
MasseObjet = 10
volume = 23
Masse_Volumique = 1000
Epsilon = 0.1
NbFacettes = 0
counter = 0


#print(len(ListeFacette))

def lecturefichier(Mat_PointA,Mat_PointB,Mat_PointC,Mat_Normales,file) :
    ListeFacette = []
    #>>
    #CREATION D'UNE LISTE CONTENANT CHAQUE LIGNE DU FICHIER STL
    for line in file :
        ListeFacette.append(line.strip())
    #print(ListeFacette)
    file.close()

    A = 1
    B = 2
    C = 3
    N = 0
    counter = 0
    NbFacettes = 0
    while counter <= (len(ListeFacette)-7):
        NbFacettes += 1
        #print("Je rentre dans la boucle :")

#>>
        New_Liste.append(ListeFacette[counter])
        #print(counter)
        #print(ListeFacette[counter])
        ligne = New_Liste[N].split(" ")
        #print(ligne)
        #print('  ')
        #print('>> Nouvelle Facette : ')
        #print(' Normale : ')
        Xn = float(ligne[2])
        #print("Xn =", Xn)
        Yn = float(ligne[3])
        #print("Yn =", Yn)
        Zn = float(ligne[4])
        #print("Zn =", Zn)
        N += 4
        #print("  ")

        Normale = np.array([Xn,Yn,Zn])
        #print(Normale)
        Mat_Normales = np.vstack((Mat_Normales,Normale))


    #>>
        New_Liste.append(ListeFacette[counter+2])
        #print(ListeFacette[counter+2])
        ligne_a = New_Liste[A].split(" ")
        Xa = float(ligne_a[1])
        Ya = float(ligne_a[2])
        Za = float(ligne_a[3])
        #print("Xa =",Xa)
        #print("Ya =",Ya)
        #print("Za =",Za)
        A += 4
        #print("  ")
        pointA = np.array([Xa,Ya,Za])
        Mat_PointA = np.vstack((Mat_PointA,pointA))


    #>>
        New_Liste.append(ListeFacette[counter+3])
        #print(ListeFacette[counter+3])
        ligne_b = New_Liste[B].split(" ")
        Xb = float(ligne_b[1])
        Yb = float(ligne_b[2])
        Zb = float(ligne_b[3])
        #print("Xb =",Xb)
        #print("Yb =",Yb)
        #print("Zb =",Zb)
        B += 4
        #print("  ")
        pointB = np.array([Xb,Yb,Zb])
        Mat_PointB = np.vstack((Mat_PointB,pointB))



    #>>
        New_Liste.append(ListeFacette[counter+4])
        #print(ListeFacette[counter+4])
        ligne_c = New_Liste[C].split(" ")
        #print(ligne_c)
        Xc = float(ligne_c[1])
        Yc = float(ligne_c[2])
        Zc = float(ligne_c[3])
        #print("Xc =",Xc)
        #print("Yc =",Yc)
        #print("Zc =",Zc)
        C += 4
        #print("  ")
        pointC = np.array([Xc,Yc,Zc])
        Mat_PointC = np.vstack((Mat_PointC,pointC))

        counter += 7

    print("Coordonnées des normales",Mat_Normales)
    print("Coordonnées des points A",Mat_PointA)
    print("Coordonnées des points B",Mat_PointB)
    print("Coordonnées des points C",Mat_PointC)
    return (Mat_PointA,Mat_PointB,Mat_PointC,Mat_Normales,NbFacettes)



#>>>>>>>>>>>>CALCUL DE LA SURFACE D'UNE FACETTE<<<<<<<<<<<<
def surface(Mat_PointA,Mat_PointB,Mat_PointC,NbFacettes,Liste_Surface):
    i = 1
    #print(NbFacettes)
    while i <= NbFacettes :
        #print('ok')
        A = float(Mat_PointB[i,0]) - float(Mat_PointA[i,0])
        #print("A = ",A)
        B = float(Mat_PointB[i,1]) - float(Mat_PointA[i,1])
        #print("B =",B)
        C = float(Mat_PointB[i,2]) - float(Mat_PointA[i,2])
        #print("C =",C)
        X = float(Mat_PointC[i,0]) - float(Mat_PointA[i,0])
        Y = float(Mat_PointC[i,1]) - float(Mat_PointA[i,1])
        Z = float(Mat_PointC[i,2]) - float(Mat_PointA[i,2])
        i += 1
        Surface_Facette = (( (B*Z)-(C*Y) )**2 + ( (C*X)-(A*Z) )**2 + ( (A*Y)-(B*X))**2)**0.5
        Liste_Surface.append(Surface_Facette)
        #for elt in Liste_Surface :
        #    elt+=elt
        #print(elt)
    print ("Surface =",Liste_Surface)
    return Liste_Surface





#>>>>>>>>>>CALCUL DE L'ALTITUDE D'UNE FACETTE<<<<<<<<<<<
def altitude (Mat_PointA,Mat_PointB,Mat_PointC,Liste_Altitude) :
    i = 1
    NbFacettes = len(Mat_PointA)
    while i <= NbFacettes :
        Za = float(Mat_PointA[i,2])
        Zb = float(Mat_PointB[i,2])
        Zc = float(Mat_PointC[i,2])
        Altitude_Facette = 1/3*(Za+Zb+Zc)
        #print('Za=',Za)
        #print('Zb=',Zb)
        #print('Zc=',Zc)
        #print(Altitude_Facette)
        Liste_Altitude.append(Altitude_Facette)
        i+=1
        #print('ok')
        print ("Altitude =", Liste_Altitude)
    return Liste_Altitude




#>>>>>>>>>RECHERCHE DU POINT LE PLUS BAS<<<<<<<<<<
def Zmin(Liste_Altitude):
    i = 0
    Zmin = Liste_Altitude[0]
    print(len(Liste_Altitude))
    while i < len(Liste_Altitude):
        print('ok')
        if Liste_Altitude[i] <= Zmin :
            Zmin = Liste_Altitude[i]
            i += 1
        else :
            Zmin = Zmin
            i += 1
            print(Zmin)
    return Zmin
    #print("Le point le plus bas est à", Zmin)


def Zmax(Liste_Altitude):
    i = 0
    Zmax = Liste_Altitude[0]
    while i <= len(Liste_Altitude)-1 :
        if Liste_Altitude[i] >= Zmax :
            Zmax = Liste_Altitude[i]
            i += 1
        else :
            Zmax = Zmax
            i += 1
    return Zmax
#>>>>>>>>>>CALCUL DES COORDONNÉES DE LA NORMALE D'UNE FACETTE<<<<<<<<<<<<
def normale(Mat_Normales,NbFacettes):
    i = 1
    while i <= NbFacettes :
        Xn = float(Mat_Normales[i,0])
        Yn = float(Mat_Normales[i,1])
        Zn = float(Mat_Normales[i,2])
        Xn_Normale = Xn
        Yn_Normale = Yn
        Zn_Normale = Zn
        i+=1
        Liste_N_Normale.append(Xn)
        Liste_N_Normale.append(Yn)
        Liste_N_Normale.append(Zn)
    return Liste_N_Normale
    #print(Liste_N_Normale)



    #Normale_Facette = np.array([Xn,Yn,Zn])



#>>>>>>>>>CALCUL DE LA POUSSEE D'ARCHIMEDE<<<<<<<<<<<<<<<<<
def calculFa(Liste_N_Normale,Liste_Force_FaXn,Liste_Force_FaYn,Liste_Force_FaZn,Masse_Volumique,gravity):
    #print(Liste_N_Normale)
    i = 0
    j = 0
    k = 0
    sumFaXn = 0
    sumFaYn = 0
    sumFaZn = 0
    #print(len(Liste_N_Normale))
    #print(len(Liste_Altitude))
    #print(len(Liste_Surface))
    print("liste Zg",Liste_Zg)
    print("listeAltitude Archimede",Liste_Altitude)
    while i <= len(Liste_N_Normale)-3 and j <= len(Liste_Altitude)-1 and k <= len(Liste_Surface)-1 :
        #print('ok')
        Xn = Liste_N_Normale[i]
        Yn = Liste_N_Normale[i+1]
        Zn = Liste_N_Normale[i+2]
        #print("norme de la normale",normale)
        altitude = Liste_Altitude[j]
        #print("altitude =",altitude)
        surface = Liste_Surface[k]
        #print("surface =",surface)
        #Force_A = (Xn*float(Liste_Surface[i])*float(Liste_Altitude[j]),Yn*float(Liste_Surface[i])*float(Liste_Altitude[j]),Zn*float(Liste_Surface[i])*float(Liste_Altitude[j]))
        sumFaXn += Xn*float(Liste_Surface[k])*float(Liste_Altitude[j])
        sumFaYn += Yn*float(Liste_Surface[k])*float(Liste_Altitude[j])
        sumFaZn += Zn*float(Liste_Surface[k])*float(Liste_Altitude[j])
        i += 3
        j += 1
        k += 1
        Liste_Force_FaXn.append(sumFaXn)
        Liste_Force_FaYn.append(sumFaYn)
        Liste_Force_FaZn.append(sumFaZn)
    sumFaXn = sumFaXn*Masse_Volumique*gravity
    sumFaYn = sumFaYn*Masse_Volumique*gravity
    sumFaZn = sumFaZn*Masse_Volumique*gravity
    NormeVectForceArchimede = (((sumFaXn)**2)+((sumFaYn)**2)+((sumFaZn)**2))**0.5

    print(NormeVectForceArchimede)
    return NormeVectForceArchimede
    #print(Liste_Force_FaXn)
    #print(Liste_Force_FaYn)
    #print(Liste_Force_FaZn)

    #print(sumFaXn)
    #print(sumFaYn)
    #print(sumFaZn)

    #print("Fa(X) = ",sumFaXn*gravity*Masse_Volumique)
    #print("Fa(Y)=",sumFaYn*gravity*Masse_Volumique)
    #print("Fa(Z) =",sumFaZn*gravity*Masse_Volumique)



    #print("somme =",sumFa)
def CalculPoids(MasseObjet,gravity) :
    Poids_Objet = MasseObjet*gravity
    return Poids_Objet

#>>>>>>>>CALCUL DU MOUVEMENT DE TRANSLATION<<<<<<<<<<<
def translation(Liste_Altitude,ecart):

    i = 0
    while i <= len(Liste_Altitude)-1 :

               Liste_Altitude[i] += ecart
               i += 1

    print("new =",Liste_Altitude)
    return Liste_Altitude



def dichotomie(Zmax,Epsilon,forcePoids,forceArchimede,Liste_Altitude,MasseObjet,gravity):
    Zmax=Zmax(Liste_Altitude)
    Zb= 0
    Za = -Zmax

    print(Za)
    forceArchimede = calculFa(Liste_N_Normale,Liste_Force_FaXn,Liste_Force_FaYn,Liste_Force_FaZn,Masse_Volumique,gravity)
    print("force archi",forceArchimede)
    poids = CalculPoids(MasseObjet,gravity)
    counter = 0
    ecart = 0


    while abs(poids - forceArchimede)>Epsilon and counter < 10:
        counter+=1
        print(">>>>>>>>itération   ",counter)
        print('OK')
        Zg= (Zb + Za)/2
        print("      Zg_dicho     ",Zg)

        if (poids-forceArchimede)>Epsilon:
            ecart= Za-Zg
            print("ecart", ecart)
            print("listeAltitude",Liste_Altitude)
            translation(Liste_Altitude,ecart)
            print("listeAltitude",Liste_Altitude)
            forceArchimede = calculFa(Liste_N_Normale,Liste_Force_FaXn,Liste_Force_FaYn,Liste_Force_FaZn,Masse_Volumique,gravity)
            print("     force archimède      ", forceArchimede)
            Za= Zg
            print("     if    ",Zg)


        elif (poids-forceArchimede )<Epsilon:
            ecart= Zb-Zg
            print("ecart", ecart)
            print("listeAltitude",Liste_Altitude)
            translation(Liste_Altitude,ecart)
            print("listeAltitude",Liste_Altitude)
            forceArchimede = calculFa(Liste_N_Normale,Liste_Force_FaXn,Liste_Force_FaYn,Liste_Force_FaZn,Masse_Volumique,gravity)
            Zb =Zg
            print("     elif       ",Zg)

        else :
            print("Le bateau est à l'équilibre")
            print("     else       ",Zg)

    return Zg








#>>
#ON PARCOURS TOUTE LA LISTE EN DEPOSANT DANS UNE AUTRE LISTE SEULEMENT LES LIGNES QUI NOUS INTERESSENT
#ENSUITE ON GARDE SEULEMENT LES VALEURS DES COORDONNEES (ON NE GARDE QUE LES CHIFFRES)

if __name__ == '__main__':

    #>>
    #CREATION D'UNE FIGURE
    #figure = pyplot.figure()
    #axes = mplot3d.Axes3D(figure)



    #>>
    #TRACAGE DE LA FIGURE 3D
    #your_mesh = mesh.Mesh.from_file('/Users/eloiselefebvre/Desktop/Projet 2e année/V_HULL_Normals_Outward.STL')
    #axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

    #scale = your_mesh.points.flatten(-1)
    #axes.auto_scale_xyz(scale, scale, scale)

    #>>>>>>>>>pyplot.show()

    print("Début de récupération des données >>>>>>")

    #>>
    #OUVERTURE ET LECTURE DU FICHIER STL
    file = open('/Users/eloiselefebvre/Desktop/Projet 2e année/V_HULL_Normals_Outward.STL','r')
    file.readline()



    Mat_PointA,Mat_PointB,Mat_PointC,Mat_Normales,NbFacettes = lecturefichier(Mat_PointA,Mat_PointB,Mat_PointC,Mat_Normales,file)


    #>>
    #CALCUL DE LA SURFACE
    surface(Mat_PointA,Mat_PointB,Mat_PointC,NbFacettes,Liste_Surface)

    #>>
    #CALCUL DE L'ALTITUDE
    altitude(Mat_PointA,Mat_PointB,Mat_PointC,Liste_Altitude)

    #>>
    #CALCUL DU POINT LE PLUS BAS
    Zmin(Liste_Altitude)

    #>>
    #RECUPERATION DES COORDONNEES DE LA NORMALE
    #vect_Normale = normale(Mat_Normales,NbFacettes)

    #>>
    #>>>>>>>>>>>CALCUL DE LA POUSSEE D'ARCHIMEDE POUR LES FACETTES IMMERGEES<<<<<<<<<<<<<
    #calculFa(Liste_N_Normale,Liste_Force_FaXn,Liste_Force_FaYn,Liste_Force_FaZn,gravity,Masse_Volumique)


    #translation(Liste_N_Normale,Liste_Force_FaXn,Liste_Force_FaYn,Liste_Force_FaZn,Masse_Volumique,gravity,MasseObjet)
    #forcePoids = CalculPoids(MasseObjet,gravity)
    #forceArchimede = calculFa(Liste_N_Normale,Liste_Force_FaXn,Liste_Force_FaYn,Liste_Force_FaZn,Masse_Volumique,gravity)
    #dichotomie(Zmax,Epsilon,forcePoids,forceArchimede,Liste_Altitude,MasseObjet,gravity)
    #print("Le point le plus bas est à z =",Zmin(Liste_Altitude))
    #print(Liste_Altitude)
    #print(Liste_Fa)




    #print (Mat_Normales)
    #print(New_Liste)

import math
from math import floor
count_del = 2
count_ins = 2
count_sub_max = 4 #si on change dans count_sub, il faut changer count_sub_max

def count_sub(a, b):
    if a == b :
        return 0
    if (a == 'A' and b == 'T') or (a == 'T' and b == 'A') or (a == 'G' and b == 'C') or (a == 'C' and b == 'G') :
    	return 3
    return 4 

def dist_naif(x, y):
    return dist_naif_rec(x, y, 0, 0, 0, math.inf)

def dist_naif_rec(x, y, i, j, cout, dist):
    """x et y deux mots,
    i un indice dans [0..|x|], j un indice dans [0..|y|],
    cout le coût de l'alignement de (x[1..i],y[1..j]),
    dist le coût du meilleur alignement de (x,y) connu avant cet appel
    Rend dist, le meilleur coût de l'alignement de (x,y)"""
    if i == len(x) and j == len(y) :
        if cout < dist :
            dist = cout
    else:
        if i < len(x) and j < len(y) :
            dist = dist_naif_rec(x, y, i+1, j+1, cout+count_sub(x[i], y[j]), dist)
        if i < len(x) :
            dist = dist_naif_rec(x, y, i+1, j, cout+count_del, dist)
        if j < len(y) :
            dist = dist_naif_rec(x, y, i, j+1, cout+count_ins, dist)
    return dist

def get_with_fichier(fichier):
    f=open("./Instances_genome/"+fichier, "r")
    nb_x = f.readline()
    nb_y = f.readline()
    x = f.readline()
    y = f.readline()
    x_return = ""
    y_return = ""
    for i in x: #Enlever les espaces
    	i = i.replace(" ","")
    	i = i.strip()
    	x_return = x_return + i
    for i in y: #Enlever les espaces
    	i = i.replace(" ","")
    	i = i.strip()
    	y_return = y_return + i
    f.close()
    return (x_return,y_return) #renvoi les mots x et y du fichier

def dist_1(x,y):
    tableau = [] 
    #initialisation tableau[][] à 0
    for i in range(len(x)+1):
        tableau.append([0] * (len(y)+1))

	#initialisation des colonnes et des lignes d'indices [i][0] ou [0][i] dans le tableau
    for i in range(len(x)+1):
        tableau [i][0] = i*count_del #ligne D(i,0)
    for i in range(len(y)+1):
        tableau [0][i] = i*count_ins #colonne D(0,i)
        
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            case_haut = tableau[i-1][j]
            case_gauche = tableau[i][j-1]
            case_haut_gauche = tableau[i-1][j-1]
            tableau[i][j] = min(case_haut+count_del, case_gauche+count_ins, case_haut_gauche+count_sub(x[i-1],y[j-1]))
	                    
    # AFFICHAGE DU TABLEAU [][]
    #for i in range(len(x)+1):
    #    print(tableau[i])
    # AFFICHAGE DU TABLEAU [][]
    return tableau[len(x)][len(y)]


def dist_2(x,y):

	tableau = []
	#initialisation tableau[][] à 0
	for i in range(2):
		tableau.append([0] * (len(y)+1))
	tableau_vide=[0 for j in range(len(y)+1)] 

	#initialisation du tableau
	for j in range(1,len(y)+1): #la ligne 0
		tableau[0][j] = j*count_ins #colonne D(0,j)
	
	for i in range(1,len(x)+1):
		tableau[1][0] = count_del * i
		for j in range(1,len(y)+1):
			case_haut = tableau[0][j]
			case_gauche = tableau[1][j-1]
			case_haut_gauche = tableau[0][j-1]
			tableau[1][j] = min(case_haut+count_del, case_gauche+count_ins, case_haut_gauche+count_sub(x[i-1],y[j-1]))

		for j in range(0,len(y)+1):
			tableau[0][j]=tableau[1][j]
		
		tableau[1]=tableau_vide
	#tableau[0] = derniere ligne contenant le meilleur 
	t = tableau[0]
	#print(tab[0])
	#print("meilleur alignement : ", t[len(t)-1])
	return t[len(t)-1]

def get_tableau(x,y):
    tableau = []
    #initialisation tableau[][] à 0
    for i in range(len(x)+1):
        tableau.append([0] * (len(y)+1))

    #initialisation des colonnes et des lignes d'indices [i][0] ou [0][i] dans le tableau
    for i in range(len(x)+1):
        tableau [i][0] = i*count_del #ligne D(i,0)
    for i in range(len(y)+1):
        tableau [0][i] = i*count_ins #colonne D(0,i)

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            case_haut = tableau[i-1][j]
            case_gauche = tableau[i][j-1]
            case_haut_gauche = tableau[i-1][j-1]
            tableau[i][j] = min(case_haut+count_del, case_gauche+count_ins, case_haut_gauche+count_sub(x[i-1],y[j-1]))

    # AFFICHAGE DU TABLEAU [][]
    #for i in range(len(x)+1):
    #	print(tableau[i])
    # AFFICHAGE DU TABLEAU [][]
    return tableau

def sol_1(x,y,tableau):
    x_return = ""
    y_return = ""
    i = len(x)
    j = len(y)
    #print(tableau[i][j])
    while(i > 0 or j > 0):
        #print("indice i = ", i)
        #print("indice j = ", j)
        indice_courant = tableau[i][j]
        case_haut = tableau[i-1][j]
        case_gauche = tableau[i][j-1]
        case_haut_gauche = tableau[i-1][j-1]
        if(indice_courant-case_haut == indice_courant-case_gauche):
        	if(indice_courant-case_haut == count_del):
        		x_return = x_return + x[i-1]
        		y_return = y_return + "-"
        		i = i - 1
        #case precedente
        elif(indice_courant-case_haut == count_del):
            x_return = x_return + x[i-1]
            y_return = y_return + "-"
            i = i - 1
        elif(indice_courant-case_gauche == count_ins):
            x_return = x_return + "-"
            y_return = y_return + y[j-1]
            j = j - 1
        if(indice_courant-case_haut_gauche == count_sub(x[i-1],y[j-1])):
            x_return = x_return + x[i-1]
            y_return = y_return + y[j-1]
            i = i - 1
            j = j - 1
    ali_x=""
    ali_y=""
    #renverser le mot pour obtenir l'alignement car on commence de la fin
    for i in reversed(x_return):
        ali_x = ali_x + i
    for j in reversed(y_return):
        ali_y = ali_y + j
    #alignement de x et y
    #print(ali_x)
    #print(ali_y)
    #alignement de x et y
    return (ali_x,ali_y)

def prog_dyn(x,y):
    #print(x)
    #print(y)
    alignement = sol_1(x,y,get_tableau(x,y))
    distance_edition = dist_1(x,y)
    return(distance_edition,alignement)

def prog_dyn2(x,y):
    #print(x)
    #print(y)
    alignement = sol_1(x,y,get_tableau(x,y))
    distance_edition = dist_2(x,y)
    return(distance_edition,alignement)

def mots_gap(k):
    return "-"*k
#print(mots_gap(5))

def align_lettre_mot(x,y):
    indice = 0
    min = count_sub_max
    L=""
    for i in range (len(y)):
        if(min>count_sub(x,y[i])):
            min = count_sub(x,y[i])
            indice = i
            #print(x)
            #print(y)
            #print(indice)
    L = L + mots_gap(indice)
    L = L + x
    L = L + mots_gap(len(y)-indice -1)
    return L

def coupure(x,y):
	x_gauche = ""
	x_droite = ""
	y_gauche = ""
	y_droite = ""
	l = len(x)
	m = len(y)
	for i in range(0,m+1):
		x_gauche = x_gauche + x[0:floor(l/2)]
		x_droite = x_droite + x[floor(l/2):l]
		y_gauche = y_gauche + y[0:i]
		y_droite = y_droite + y[i:l]
		#print("x_gauche : ",x_gauche)
		#print("y_gauche : ",y_gauche)
		#print("x_droite : ",x_droite)
		#print("y_droite : ",y_droite)

		if dist_2(x_gauche,y_gauche) + dist_2(x_droite,y_droite) == dist_2(x,y):
			#print("ON EST RENTRER ICI")
			return i #indice de la coupure Y
		#remit à null pour éviter de garder l'ancienne valeur
		x_gauche = ""
		x_droite = ""
		y_gauche = ""
		y_droite = ""
	#print("ON EST SORTI DE COUPURE")



def Sol_2(x,y):
	#pour les appels recursifs
	#print("on PRINT LEN DE X : ",len(x))
	#print(x)
	#print("on PRINT LEN DE Y : ",len(y))
	#print(y)
	gauche=[]
	droitee=[]
	if((len(x)==0) and (len(y)>0)):
		#print("CAS 1111111111111111")
		return [mots_gap(len(y)),y]
	if((len(x)>0) and (len(y)==0)):
		#print("CAS 2222222222222222")
		return [x,mots_gap(len(x))]
	if((len(x) == 0) and (len(y) == 0)):
		#print("CAS 3333333333333333")
		return []
	if (len(x)==1) and (len(y) > 0):
		#print("CAS 4444444444444444")
		return [align_lettre_mot(x,y),y]
	if(len(x) > 1 and len(y) >= 1):
		h=floor(len(x)/2) # indice de la coupure de X
		k=coupure(x,y) # indice de la coupure de Y
		#print("CAS 5555555555555555")
		#print(h) 
		#print(k)
		gauche=[Sol_2(x[:h],y[:k])]
		droitee=[Sol_2(x[h:],y[k:])]
		
		return gauche[0]+droitee[0]


def Sol_2_2(x,y):
	x_res=""
	y_res=""
	resultat = Sol_2(x,y)
	cpt = len(resultat)
	for i in resultat:
		if cpt%2 == 0:
			x_res = x_res + i
		else:
			y_res = y_res + i
		cpt = cpt - 1
	return x_res,y_res
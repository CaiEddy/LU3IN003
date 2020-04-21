from Alignement import *
import sys
import time
sys.setrecursionlimit(7000) #sinon le systeme stop le programme (trop d'appel)
tableau_fichier_instance=["Inst_0000010_44.adn","Inst_0000010_8.adn","Inst_0000010_7.adn","Inst_0000012_13.adn",\
						"Inst_0000012_32.adn","Inst_0000012_56.adn","Inst_0000014_83.adn","Inst_0000013_45.adn",\
						"Inst_0000013_56.adn","Inst_0000013_89.adn","Inst_0000014_7.adn","Inst_0000015_4.adn",\
						"Inst_0000015_2.adn","Inst_0000015_76.adn","Inst_0000020_32.adn","Inst_0000020_17.adn",\
						"Inst_0000020_8.adn","Inst_0000050_3.adn","Inst_0000050_9.adn","Inst_0000050_77.adn",\
						"Inst_0000100_3.adn","Inst_0000100_7.adn","Inst_0000100_44.adn","Inst_0000500_3.adn",\
						"Inst_0000500_8.adn","Inst_0000500_88.adn","Inst_0001000_7.adn","Inst_0001000_23.adn",\
						"Inst_0001000_2.adn","Inst_0002000_8.adn","Inst_0002000_3.adn","Inst_0002000_44.adn",\
						"Inst_0003000_25.adn","Inst_0003000_45.adn","Inst_0003000_10.adn","Inst_0003000_1.adn",\
						"Inst_0005000_4.adn","Inst_0005000_33.adn","Inst_0005000_32.adn","Inst_0008000_98.adn",\
						"Inst_0008000_54.adn","Inst_0010000_8.adn","Inst_0010000_50.adn","Inst_0010000_7.adn",\
						"Inst_0015000_20.adn","Inst_0015000_30.adn","Inst_0015000_3.adn","Inst_0020000_77.adn",\
						"Inst_0020000_5.adn","Inst_0020000_64.adn","Inst_0050000_6.adn","Inst_0050000_63.adn",\
						"Inst_0050000_88.adn","Inst_0100000_3.adn","Inst_0100000_11.adn","Inst_0100000_76.adn",]

################################# TACHE A #################################
################################# TACHE A #################################
################################# TACHE A #################################

print("TACHE_A\n")
print("Tester la validité de votre implémentation sur les instances Inst_0000010_44.adn,\
Inst_0000010_7.adn et Inst_0000010_8.adn qui ont pour distance d'édition 10, 8 et 2.\n")


test=get_with_fichier("Inst_0015000_3.adn")
x=test[0]
y=test[1]
print("Test pour Inst_0015000_3.adn avec x = "+x+" et y = "+y)
start_time = time.time()
print("Distance d'edition :",prog_dyn(x,y))
print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))

test=get_with_fichier("Inst_0000010_7.adn")
x=test[0]
y=test[1]
print("Test pour Inst_0000010_7.adn avec x = "+x+" et y = "+y)
start_time = time.time()
print("Distance d'edition : ",dist_naif(x,y))
print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))

test=get_with_fichier("Inst_0000010_8.adn")
x=test[0]
y=test[1]
print("Test pour Inst_0000010_8.adn avec x = "+x+" et y = "+y)
start_time = time.time()
print("Distance d'edition : ",dist_naif(x,y))
print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))


#enlever les ("") pour effecter les calcules pour évaluer les performances
"""
# GROS GROS RECURSION ATTENTION 
# GROS GROS RECURSION ATTENTION 
print("Pour évaluer les performances de cette méthode, évaluez jusqu'à quelle taille d'instance vous pouvez\
résoudre les instances fournies en moins d'une minute.\n")
print("VOIR DOSSIER")

for i in tableau_fichier_instance:
	test=get_with_fichier(i)
	x=test[0]
	y=test[1]
	print("Test pour ",i,"avec x = "+x+" (",len(x),")"" et y = "+y+" (",len(y),")")
	start_time = time.time()
	print("Distance d'edition :",dist_naif(x,y))
	print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))
"""

################################# TACHE B #################################
################################# TACHE B #################################
################################# TACHE B #################################
print("TACHE_B\n")
print("Coder les deux fonctions DIST_1 et SOL_1, ainsi qu'une fonction PROG_DYN qui prend en entrée\
seulement les mots x et y et\n qui renvoie à la fois la distance d(x; y) et un alignement optimal. Tester\
ces fonctions sur plusieurs instances.")
print("Avec DIST_1\n")
print("VOIR DOSSIER")

#enlever les ("") pour effecter les calcules pour évaluer les performances
"""
for i in tableau_fichier_instance:
	test=get_with_fichier(i)
	x=test[0]
	y=test[1]
	print("Test pour ",i,"avec x = "+x+" (",len(x),")"" et y = "+y+" (",len(y),")")
	start_time = time.time()
	print("Distance d'edition :",prog_dyn(x,y))
	#prog_dyn(x,y)
	#print(len(x))
	print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))
"""

################################# TACHE C #################################
################################# TACHE C #################################
################################# TACHE C #################################
print("TACHE_C\n")
print("Tracer la courbe de consommation de temps CPU en fonction de la taille jxj du premier mot du\
couple des instances fournies.\n Est-ce que la courbe obtenue correspond à la complexité théorique ?")
print("Avec DIST_2\n")
print("VOIR DOSSIER")


#enlever les ("") pour effecter les calcules pour évaluer les performances
"""
for i in tableau_fichier_instance:
	test=get_with_fichier(i)
	x=test[0]
	y=test[1]
	print("Test pour ",i,"avec x = "+x+" (",len(x),")"" et y = "+y+" (",len(y),")")
	start_time = time.time()
	print("Distance d'edition :",prog_dyn2(x,y))
	#prog_dyn2(x,y)
	#print(len(x))
	print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))
"""

################################# TACHE D #################################
################################# TACHE D #################################
################################# TACHE D #################################
print("TACHE_D\n")
print("Tracer la courbe de consommation de temps CPU en fonction de la taille jxj du premier mot du\
couple des instances fournies.\n Vous pouvez vous limiter aux instances nécessitant moins de 10 minutes\
chacune.")
print("Avec DIVISER POUR REGNER\n")
print("VOIR DOSSIER")

#enlever les ("") pour effecter les calcules pour évaluer les performances
"""
for i in tableau_fichier_instance:
	test=get_with_fichier(i)
	x=test[0]
	y=test[1]
	print("Test pour ",i,"avec x = "+x+" (",len(x),")"" et y = "+y+" (",len(y),")")
	start_time = time.time()
	print("Le meilleur alignement est : ",Sol_2_2(x,y))
	#Sol_2_2(x,y)
	#print(len(x))
	print("Temps d execution : %.6s secondes\n" % (time.time() - start_time))
"""
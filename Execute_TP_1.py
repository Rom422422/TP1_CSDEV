# Header
'''
Que fait le programme : Il sert de calendrier, annonce si l'année est bisextile, le nombre de jour d'un mois,
si la date existe.
Qui l'a fait : Thibaut Romain
Quand à t'il était réalisé : 25/09/2023 
Que reste-t-il à faire : Fait
'''
#Importation des bibilotheque 
from Code_TP_1 import annee_bisextile as ann_bi
from Code_TP_1 import nb_jour as nb_jour
from Code_TP_1 import date_valide as date_valide



#Test fonction anne_bisextile
print("L'année 2020 est bisextile : True -> ", ann_bi(2020))
print("L'année 2021 est bisextile : False -> ", ann_bi(2021))
print("L'année 2100 est bisextile : False -> ", ann_bi(2100))
print("L'année 2400 est bisextile : True -> ", ann_bi(2400))
print("L'année deux milles vingt est bisextile : Vous n'avez pas selectionné une année en chiffre entier. -> ", ann_bi("deux milles vingt"))

#Test fonction nb_jour
print("Le mois 1 de l'année 2000 a combien de jour: 31 -> ", nb_jour(1,2000))
#print("Le mois Janvier de l'année 2000 a combien de jour: 31 -> ", nb_jour("Janvier",2000))
print("Le mois 4 de l'année 2000 a combien de jour: 30 -> ", nb_jour(4,2000))
print("Le mois 2 de l'année 2100 a combien de jour: 28 -> ", nb_jour(2,2100))
print("Le mois 2 de l'année 2020 a combien de jour: 29 -> ", nb_jour(2,2020))
#print("Le mois Février de l'année 2020 a combien de jour: Veuillez selectionner le mois en chiffre. mars = 5 par exemple -> ", nb_jour("Février",2020))

#Test fonction date_valide
print("La date 11/4/2003 existe : True -> :", date_valide(11,4,2003))
print("La date 28/2/2010 existe : True -> :", date_valide(28,2,2010))
print("La date 29/2/2020 existe : True -> :", date_valide(29,2,2020))
print("La date 31/1/234 existe : True -> :", date_valide(31,1,234))
print("La date 29/2/2021 existe : False -> :", date_valide(29,2,2021))
print("La date 1/31/234 existe : False -> :", date_valide(1,31,234))
print("La date 33/12/13 existe : False -> :", date_valide(13,13,13))
print("La date 31/11/234 existe : False -> :", date_valide(31,11,234))
print("La date 30/2/234 existe : False -> :", date_valide(30,2,234))

#Programme principale 
'''
Programme qui propose la saisie d'une date , la valide et affiche si elle est valide.
'''
'''Jour, Mois, Annee = int(input("Veuillez rentrer le jour : ")), int(input("Veuillez rentrer le mois : ")),int(input("Veuillez rentrer l'année : "))
Verif = date_valide(Jour, Mois, Annee)
if Verif == True: 
    print("Date valide")
else:
    print("Date non valide")
'''



# Header
'''
Que fait le programme : Il calcule les impots d'une personnne célibataire
Qui l'a fait : Thibaut Romain
Quand à t'il était réalisé : 25/09/2023 
Que reste-t-il à faire : Faire en sorte que le programme tronque a l'inférieur
'''
#Importation des bibilotheque 
from Code_TP_1 import mesImpots as mesImpots

'''revenu = int(input("Quelles sont vos revenus? en entier : "))
print("Vous serez taxez de : ", mesImpots(revenu), "$")'''

# Header
'''
Que fait le programme : Il calcule les impots d'une personnne célibataire
Qui l'a fait : Thibaut Romain
Quand à t'il était réalisé : 25/09/2023 
Que reste-t-il à faire : Faire en sorte que le programme tronque a l'inférieur
'''
#Importation des bibilotheque 
from Code_TP_1 import mult_matrice as mult

M1 = [[1,0,0],[0,1,0],[0,0,1]]
M2 = [[2,2,0],[0,1,9],[56,0,1]]
M3 = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
M4 = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
#print(mult(M1,M2))
print(mult(M3,M4))




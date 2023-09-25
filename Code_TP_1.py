# Header
'''
Que fait le programme : Il sert de calendrier, annonce si l'année est bisextile, le nombre de jour d'un mois,
si la date existe.
Qui l'a fait : Thibaut Romain
Quand à t'il était réalisé : 25/09/2023 
Que reste-t-il à faire : Tout sauf point 1
'''


def annee_bisextile(annee:int)->bool:#Annonce si l'année est bisextile ou non. entré : une année. sortie : True ou False
    if type(annee) != int :
        return("Vous n'avez pas selectionné une année en chiffre entier.") 
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0


def nb_jour(mois, annee):#Retourne le nombre de jour dans le mois. Entré : année et mois. sortie : Nombre de jours
    assert isinstance(mois, int) and 1 <= mois <= 12 , "Veuillez selectionner le mois en chiffre inferieur à douze. mars = 5 par exemple"
    if mois == 2:
        if annee_bisextile(annee) == True:
            return 29
        return 28
    elif mois in [4, 6, 9, 11]:
        return 30
    return 31   

def date_valide(jour, mois, annee):#Analyse la date pour verifier si elle existe. Entré : jour, mois, année. Sortie : True or False
    assert isinstance(mois, int) , "Veuillez selectionner le mois en chiffre inferieur à douze. mars = 5 par exemple"
    assert isinstance(jour, int) , "Veuillez selectionner le jour en chiffre inferieur à 31. mars = 5 par exemple"
    assert isinstance(annee, int), "Veuillez selectionner le jour en chiffre"
    if mois == 2:
        if (annee_bisextile(annee) == True and jour <= 29) or (annee_bisextile(annee) == False and jour <= 28):
            return True
    elif mois in [4, 6, 9, 11] and jour <= 30:
        return True
    elif jour <= 31:
        return True
    return False



# Header
'''
Que fait le programme : Il calcule les impots d'une personnne célibataire
Qui l'a fait : Thibaut Romain
Quand à t'il était réalisé : 25/09/2023 
Que reste-t-il à faire : 
'''
#Importation des bibilotheque
from math import floor

def mesImpots(revenu):
    assert isinstance(revenu, int), "Chiffre entier uniquement wesh"
    if 10226 <= revenu <= 26070:
        return floor((revenu - 10225) * 11 / 100)
    elif 26071 <= revenu <= 74545:
        return floor((revenu - 26070) * 30 / 100 + (26070 - 10225) * 11 / 100)
    elif 74546 <= revenu <= 160336:
        return floor((revenu - 74545) * 41 / 100 + (74545 - 26070) * 30 / 100 + (26070 - 10225) * 11 / 100)
    elif 160336 <= revenu:
        return floor((revenu- 160336) * 45 / 100 + (160336 - 74545) * 41 / 100 + (74545 - 26070) * 30 / 100 + (26070 - 10225) * 11 / 100)
    return 0    

# Header
'''
Que fait le programme : Multiplication des matrices
Qui l'a fait : Thibaut Romain
Quand à t'il était réalisé : 25/09/2023 
Que reste-t-il à faire : Tout
'''

def mult_matrice(mat1,mat2):
    valren, valeur = [[],[],[],[]], 0
    for lignem1 in range(len(mat1)):
        for colonne in range(len(mat2)):
            for ligne in range(len(mat2)):
                valeur += mat1[lignem1][ligne]*mat2[ligne][colonne]
            valren[lignem1].append(valeur)
            valeur = 0
    return valren


    




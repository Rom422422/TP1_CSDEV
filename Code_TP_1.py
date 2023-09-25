# Header
'''
Que fait le programme : Il sert de calendrier, annonce si l'année est bisextile, le nombre de jour d'un mois,
si la date existe.
Qui l'a fait : Thibaut Romain
Quand à t'il était réalisé : 25/09/2023 
Que reste-t-il à faire : Fait
'''

def annee_bisextile(annee):#Annonce si l'année est bisextile ou non
    if type(annee) != int :
        return("Vous n'avez pas selectionné une année en chiffre entier.")
    valren = False
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        valren = True
    return valren
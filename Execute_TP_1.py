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


#Test fonction anne_bisextile
print("L'année 2020 est bisextile : True -> ", ann_bi(2020))
print("L'année 2021 est bisextile : False -> ", ann_bi(2021))
print("L'année 2100 est bisextile : False -> ", ann_bi(2100))
print("L'année 2400 est bisextile : True -> ", ann_bi(2400))
print("L'année deux milles vingt est bisextile : Vous n'avez pas selectionné une année en chiffre entier. -> ", ann_bi("deux milles vingt"))

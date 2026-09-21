import json # nécessaire pour utiliser les fichiers json
import sys

# les lignes pour importer pyside6
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

small_fichier = open("data_small.json", "r") # ouvre un fichier (param1) en lecture (param2)
large_fichier = open("data_large.json", "r") # on le stocke dans une variable qui devient un objet fichier (on peut lire toute mais difficilement accéder aux données (voir methode plus bas))

# print(small_fichier.read()) # on affiche le contenu du fichier

# mais pour accéder aux variables il faut load le fichier

with open("data_small.json", "r") as small_fichier:        # with permet de ouvrir et fermer le json sans avoir a mettre open au debut et close a la fin, et dans la fonction with on a acces au fichier ouvert
    donnees_small = json.load(small_fichier) # il faut load le fichier dans une variable pour accéder aux données

# print(donnees_small) # retourne toutes les données
# print(donnees_small[0]) # retourne les données dans le 1er index
# print(donnees_small[0]["nom"]) # retourne le nom dans le 1er index des données

for i in donnees_small: # on peut boucler dans les données pour accéder aux variables de chaque index
    print(i["nom"]) # retourne tous les noms dans le fichier


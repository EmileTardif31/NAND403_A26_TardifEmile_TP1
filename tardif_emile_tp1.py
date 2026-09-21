import sys
import json # nécessaire pour utiliser les fichiers json

# ------------- PySide6 setup -------------------------

# les lignes pour importer pyside6
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem

app = QApplication(sys.argv)

# -- affiche une fenetre, mais on a juste besoin d'un tableau --
# window = QWidget() # crée une fenetre
# window.show() # affiche la fenetre

# sys.exit(app.exec())  ---- il faut mettre ca la fin du programme, et le code apres s'exécute des que la window se ferme

# ------------ Json setup ----------------

small_fichier = open("data_small.json", "r") # ouvre un fichier (param1) en lecture (param2)
large_fichier = open("data_large.json", "r") # on le stocke dans une variable qui devient un objet fichier (on peut lire toute mais difficilement accéder aux données (voir methode plus bas))

# print(small_fichier.read()) # on affiche le contenu du fichier

# mais pour accéder aux variables il faut load le fichier

with open("data_small.json", "r", encoding="utf-8") as small_fichier:        # with permet de ouvrir et fermer le json sans avoir a mettre open au debut et close a la fin, et dans la fonction with on a acces au fichier ouvert
    donnees_small = json.load(small_fichier) # il faut load le fichier dans une variable pour accéder aux données

with open("data_large.json", "r", encoding="utf-8") as large_fichier:
    donnees_large = json.load(large_fichier)

# print(donnees_small) # retourne toutes les données
# print(donnees_small[0]) # retourne les données dans le 1er index
# print(donnees_small[0]["nom"]) # retourne le nom dans le 1er index des données

# for i in donnees_small: # on peut boucler dans les données pour accéder aux variables de chaque index
#     print(i["nom"]) # retourne tous les noms dans le fichier

# -- tableau dynamique --

tableau = QTableWidget() # crée un tableau simple
tableau_choisi = donnees_small # le tableau qu'on va afficher (on change la valeur selon le tableau quon veut)

tableau.setRowCount(len(tableau_choisi)) # set le nombre de row en checkant le nombre de key dans le tableau
tableau.setColumnCount(len(tableau_choisi[0])) # set le nombre de colonnes en checkant le nombre de variables dans la 1ere key (en assumant que toutes les key ont le meme nombre de variables)

# set des noms aux colonnes
tableau.setHorizontalHeaderLabels(tableau_choisi[0].keys())

for ligne, i in enumerate(tableau_choisi):
    for colonne, k in enumerate(i):
        tableau.setItem(ligne, colonne, QTableWidgetItem(str(i[k])))

# tableau.setItem(0,0,QTableWidgetItem("Alice")) # set l'élément du tableau a la ligne 0, colonne 1, on lui donne la valeur "Alice"

tableau.show()

sys.exit(app.exec()) # -- empêche la suite du code de s'exécuter tant qu'on a pas fermé la fenêtre
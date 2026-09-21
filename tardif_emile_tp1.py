import sys
import os
import json # nécessaire pour utiliser les fichiers json

# ------------ Json setup ----------------

fichier = input("Fichier json : ") # on entre le fichier json qu'on veut inspecter

if os.path.exists(fichier): # on vérifie si le fichier existe
    print("Fichier valide.")
else:
    print("Ce fichier est introuvable ou n'existe pas.")
    exit() # on ferme le programme si le fichier 

# small_fichier = open(fichier, "r") # ouvre un fichier (param1) en lecture (param2)
poids_small = os.path.getsize(fichier) / 1024 # obtient la taille du fichier en octet, on divise par 1024 pour l'avoir en Ko
# print(small_fichier.read()) # on affiche le contenu du fichier

# mais pour accéder aux variables il faut load le fichier
with open(fichier, "r", encoding="utf-8") as small_fichier:        # with permet de ouvrir et fermer le json sans avoir a mettre open au debut et close a la fin, et dans la fonction with on a acces au fichier ouvert
    donnees_small = json.load(small_fichier) # il faut load le fichier dans une variable pour accéder aux données

# print(donnees_small) # retourne toutes les données
# print(donnees_small[0]) # retourne les données dans le 1er index
# print(donnees_small[0]["nom"]) # retourne le nom dans le 1er index des données

# for i in donnees_small: # on peut boucler dans les données pour accéder aux variables de chaque index
#     print(i["nom"]) # retourne tous les noms dans le fichier

# ------------- PySide6 setup -------------------------

# les lignes pour importer pyside6
from PySide6.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem, QLineEdit, QMainWindow, QVBoxLayout, QLabel

app = QApplication(sys.argv) # crée l'application graphique pyside6 qui va permettre d'afficher l'interface

# -- affiche une fenetre, mais on a juste besoin d'un tableau --
window = QMainWindow() # crée une fenetre
window.show() # affiche la fenetre

# -- widget central qui sert de conteneur pour les autres choses
central = QWidget()
window.setCentralWidget(central)

# -- layout pour les choses dans la fenetre --
layout = QVBoxLayout()
central.setLayout(layout)
layout.setContentsMargins(10, 10, 10, 10)
layout.setSpacing(20)

# sys.exit(app.exec())  ---- il faut mettre ca la fin du programme, et le code apres s'exécute des que la window se ferme

# -- tableau dynamique --

tableau = QTableWidget() # crée un tableau simple
tableau_choisi = donnees_small # le tableau qu'on va afficher (on change la valeur selon le tableau quon veut)

tableau.setRowCount(len(tableau_choisi)) # set le nombre de row en checkant le nombre de key dans le tableau
tableau.setColumnCount(len(tableau_choisi[0])) # set le nombre de colonnes en checkant le nombre de variables dans la 1ere key (en assumant que toutes les key ont le meme nombre de variables)

# set des noms aux colonnes
tableau.setHorizontalHeaderLabels(tableau_choisi[0].keys())

# boucle pour accéder à chaque cellule
for ligne, i in enumerate(tableau_choisi):             # sort chaque élément du tableau avec l'élément stocké en i
    for colonne, k in enumerate(i):                    # sort chaque élément dans i stocké dans k
        tableau.setItem(ligne, colonne, QTableWidgetItem(str(i[k])))

tableau.setSortingEnabled(True) # debloque la fonction native de tri du tableau

# tableau.setItem(0,0,QTableWidgetItem("Alice")) # set l'élément du tableau a la ligne 0, colonne 1, on lui donne la valeur "Alice"

# tableau.show()

# -- recherche --

recherche = QLineEdit() # truc pour créer une barre de recherche
recherche.setPlaceholderText("Rechercher...")

# fonction pour afficher / retirer le texte
def update_search(texte):

    # boucle pour accéder au contenu de chaque cellule
    for ligne, i in enumerate(tableau_choisi):
        trouve = False # on se mets un bool pour arrêter la boucle si au moins 1 élément dans la ligne est correspondant
        for element, k in enumerate(i):
            if(trouve != True):
                if texte.lower() in str(i[k]).lower(): # check si le texte correspond
                    tableau.setRowHidden(ligne, False)
                    trouve = True
                elif texte == "": # check si la barre est vide
                    tableau.setRowHidden(ligne, False)
                    print("recherche vide")
                else: # si aucune correspondance on cache la ligne
                    tableau.setRowHidden(ligne, True)


recherche.textChanged.connect(update_search) # fonction appelée quand le texte change dans la barre de recherche, on valide à chaque modification

# -- infos du fichier --
infos = QLabel()
infos.setText( # change le texte a afficher dans le label (on peut mettre plusieurs fstrings pour plus de texte)
    f"Nom : {fichier}\n"
    f"Taille : {poids_small} Ko\n"
    f"Nombre d'éléments : {len(tableau_choisi)}"
)

# -- ajouter les éléments visuels au layout dans l'ordre qu'on veut
layout.addWidget(recherche) # layout.addWidget permet d'ajouter des éléments à l'interface
layout.addWidget(infos)
layout.addWidget(tableau)

sys.exit(app.exec()) # -- empêche la suite du code de s'exécuter tant qu'on a pas fermé la fenêtre
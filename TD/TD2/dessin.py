import tkinter as tk
from random import randint

# Fonctions :
def fonction_cercle():
    x = randint(60, CANVAS_WIDTH-60)
    y = randint(60, CANVAS_HEIGHT-60)
    canvas.create_oval(x-50, y+50, x+50, y-50) fill = couleur

f_cercle = fonction_cercle

def fonction_carré():
    x = randint(60, CANVAS_WIDTH-60)
    y = randint(60, CANVAS_HEIGHT-60)
    canvas.create_rectangle(x-50, y+50, x+50, y-50)

f_carré = fonction_carré

def fonction_croix():
    x = randint(10, CANVAS_WIDTH-10)
    y = randint(10, CANVAS_HEIGHT-10)
    canvas.create_line(x-50, y, x+50, y)
    canvas.create_line(x, y+50, x, y-50)

f_croix = fonction_croix

def fonction_couleur():
    global couleur
    couleur = input("Choisir une couleur")

f_couleur = fonction_couleur

# Créer la fenêtre principale:
root = tk.Tk()
root.title("Fenêtre Graphique avec Tkinter")

# Créer un bouton :
b_cercle = tk.Button(root, text="Cercle", f_cercle)
b_cercle.grid(row=1, column=0)

b_carré = tk.Button(root, text="Carré", f_carré)
b_carré.grid(row=2, column=0)

b_croix = tk.Button(root, text="Croix", f_croix)
b_croix.grid(row=3, column=0)

b_couleur = tk.Button(root, text="Couleur", f_couleur)
b_couleur.grid(row=0, column=1)

#Canva :
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Démarrer la boucle principale
root.mainloop()

import tkinter as tk
import random

# Constantes pour la taille de la fenêtre et la taille des cases
WINDOW_SIZE = 600
GRID_SIZE = 20

# Constantes pour les couleurs
BACKGROUND_COLOR = "#000000"
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"

# Création de la fenêtre principale
window = tk.Tk()
window.title("Snake")

# Création du canvas pour dessiner le jeu
canvas = tk.Canvas(window, width=WINDOW_SIZE, height=WINDOW_SIZE, background=BACKGROUND_COLOR)
canvas.pack()

# Classe représentant la nourriture
class Food:
    def __init__(self):
        # Génération aléatoire de la position de la nourriture
        self.x = random.randint(0, (WINDOW_SIZE // GRID_SIZE) - 1)
        self.y = random.randint(0, (WINDOW_SIZE // GRID_SIZE) - 1)
        self.rect = canvas.create_rectangle(self.x * GRID_SIZE, self.y * GRID_SIZE,
                                            (self.x + 1) * GRID_SIZE, (self.y + 1) * GRID_SIZE,
                                            fill=FOOD_COLOR)
        
# Classe représentant le serpent
class Snake:
    def __init__(self):
        # Initialisation de la position et de la direction du serpent
        self.x = WINDOW_SIZE // (2 * GRID_SIZE)
        self.y = WINDOW_SIZE // (2 * GRID_SIZE)
        self.dx = 1
        self.dy = 0
        self.tail = []
        # Ajout d'un nouveau carré à la fin du serpent
        for x in range(3):
            self.tail.append(canvas.create_rectangle(self.x * GRID_SIZE, self.y * GRID_SIZE,
                                                (self.x + 1) * GRID_SIZE, (self.y + 1) * GRID_SIZE,
                                                fill=SNAKE_COLOR))
        
    def move(self):
    # Déplacement du serpent en fonction de sa direction
        self.x = (self.x + self.dx) % (WINDOW_SIZE // GRID_SIZE)
        self.y = (self.y + self.dy) % (WINDOW_SIZE // GRID_SIZE)
        
        # Ajout d'un nouveau carré à la fin du serpent
        self.tail.append(canvas.create_rectangle(self.x * GRID_SIZE, self.y * GRID_SIZE,
                                                (self.x + 1) * GRID_SIZE, (self.y + 1) * GRID_SIZE,
                                                fill=SNAKE_COLOR))
        
        if (self.x, self.y) in self.tail[:-1]:
            print("Collision avec le serpent !")
            return
    
    # Suppression du premier carré du serpent (qui correspond à sa tête précédente)
        if len(self.tail) > 1:
            canvas.delete(self.tail.pop(0))

        
    def change_direction(self, dx, dy):
    # Vérification de la direction opposée à la précédente
        if self.dx == -dx and self.dy == -dy:
            return
        # Modification de la direction du serpent
        self.dx = dx
        self.dy = dy

# Création de l'objet nourriture et du serpent

food = Food()
snake = Snake()

# Fonction appelée à chaque frame pour mettre à jour le jeu
def update_game():
    # Déplacement du serpent
    snake.move()
    
    # Vérification de la collision avec la nourriture
    global food
    if snake.x == food.x and snake.y == food.y:
        # Suppression de l'objet nourriture et création d'un nouveau
        canvas.delete(food.rect)
        food = Food()
        # Ajout d'un nouveau carré à la fin du serpent
        snake.tail.append(canvas.create_rectangle(snake.x * GRID_SIZE, snake.y * GRID_SIZE,
                                                  (snake.x + 1) * GRID_SIZE, (snake.y + 1) * GRID_SIZE,
                                                  fill=SNAKE_COLOR))
    
    # Mise à jour de l'affichage
    window.update()
    
    # Appel de la fonction à la prochaine frame
    window.after(80, update_game)



# Fonction appelée lorsque l'utilisateur appuie sur une touche du clavier
def on_key_press(event):
    # Modification de la direction du serpent en fonction de la touche pressée
    if event.keysym == "Up":
        snake.change_direction(0, -1)
    elif event.keysym == "Down":
        snake.change_direction(0, 1)
    elif event.keysym == "Left":
        snake.change_direction(-1, 0)
    elif event.keysym == "Right":
        snake.change_direction(1, 0)

# Enregistrement de la fonction de gestion des touches du clavier
window.bind("<Key>", on_key_press)

# Lancement de la boucle de jeu
update_game()

# Affichage de la fenêtre
window.mainloop()



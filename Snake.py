import tkinter as tk
import random
import time
class Snake(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snake")
        self.canvas = tk.Canvas(self, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)
        self.obstacles = []
        for i in range(10):
            self.obstacles.append((random.randint(0, 19) * 20, random.randint(0, 19) * 20))
        self.direction = "Right"
        self.bind("<Key>", self.change_direction)
        self.after(100, self.game_loop)
        
    def change_direction(self, event):
        if event.keysym == "Up":
            if self.direction != "Down":
                self.direction = "Up"
        elif event.keysym == "Down":
            if self.direction != "Up":
                self.direction = "Down"
        elif event.keysym == "Left":
            if self.direction != "Right":
                self.direction = "Left"
        elif event.keysym == "Right":
            if self.direction != "Left":
                self.direction = "Right"
                
    def game_loop(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 20, self.food[1] + 20, fill="red")
        for i in range(len(self.snake)):
            self.canvas.create_rectangle(self.snake[i][0], self.snake[i][1], self.snake[i][0] + 20, self.snake[i][1] + 20, fill="white")
        for i in range(len(self.obstacles)):
            self.canvas.create_rectangle(self.obstacles[i][0], self.obstacles[i][1], self.obstacles[i][0] + 20, self.obstacles[i][1] + 20, fill="blue")
        self.move_snake()
        self.after(100, self.game_loop)
        
    def move_snake(self):
        head = self.snake[0]
        if self.direction == "Up":
            new_head = (head[0], head[1] - 20)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 20)
        elif self.direction == "Left":
            new_head = (head[0] - 20, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + 20, head[1])
        if new_head[0] < 0:
            new_head = (new_head[0] + 400, new_head[1])
        elif new_head[0] > 380:
            new_head = (new_head[0] - 400, new_head[1])
        elif new_head[1] < 0:
            new_head = (new_head[0], new_head[1] + 400)
        elif new_head[1] > 380:
            new_head = (new_head[0], new_head[1] - 400)
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)
        else:
            self.snake.pop()
        if new_head in self.snake[1:]:
            self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Helvetica", 20))
            
if __name__ == "__main__":
    game = Snake()
    game.mainloop()
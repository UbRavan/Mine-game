import tkinter as tk
import random

class DiamondGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Diamond Game")
        self.master.configure(bg="#f0f0f0")
        
        self.num_boxes = 16
        self.points = 0
        self.create_board()
        self.place_bombs_and_diamonds()
        
    def create_board(self):
        self.buttons = []
        for i in range(self.num_boxes):
            button = tk.Button(self.master, text=" ", width=8, height=3, font=("Helvetica", 12),
                               command=lambda i=i: self.reveal(i), bg="#dddddd", fg="#333333")
            button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
            self.buttons.append(button)
        
        self.score_label = tk.Label(self.master, text="Points: " + str(self.points), font=("Helvetica", 14),
                                    bg="#f0f0f0")
        self.score_label.grid(row=self.num_boxes // 4 + 1, columnspan=4, pady=10)
        
        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game, font=("Helvetica", 14),
                                        bg="#4CAF50", fg="white", padx=10, pady=5)
        self.restart_button.grid(row=self.num_boxes // 4 + 2, columnspan=4, pady=10)
        
    def place_bombs_and_diamonds(self):
        self.board = ["bomb" if random.random() < 0.5 else "diamond" for _ in range(self.num_boxes)]
        
    def reveal(self, index):
        box_type = self.board[index]
        if box_type == "bomb":
            self.buttons[index].config(text="💣", state="disabled", bg="#FF6347", fg="white")
            self.end_game()
        else:
            self.buttons[index].config(text="💎", state="disabled", bg="#7FFF00", fg="white")
            self.points += 1
            self.score_label.config(text="Points: " + str(self.points))
            if self.points == 8:
                self.end_game()
                
    def end_game(self):
        for button in self.buttons:
            button.config(state="disabled")
        if self.points == 8:
            tk.messagebox.showinfo("Game Over", "Congratulations! You found all the diamonds.")
        else:
            tk.messagebox.showinfo("Game Over", "Game over! You hit a bomb.")
            
    def restart_game(self):
        self.points = 0
        self.score_label.config(text="Points: " + str(self.points))
        for button in self.buttons:
            button.config(text=" ", state="normal", bg="#dddddd", fg="#333333")
        self.place_bombs_and_diamonds()

def main():
    root = tk.Tk()
    game = DiamondGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

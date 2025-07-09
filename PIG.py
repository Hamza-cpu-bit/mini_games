import tkinter as tk
from tkinter import messagebox
import random

class PigGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🐷 Pig Dice Game")
        self.root.geometry("400x300")

        self.scores = [0, 0]
        self.turn_score = 0
        self.current_player = 0

        self.info = tk.Label(root, text="Player 1's Turn", font=("Arial", 14))
        self.info.pack(pady=10)

        self.die_label = tk.Label(root, text="🎲 Roll: -", font=("Arial", 16))
        self.die_label.pack(pady=10)

        self.turn_score_label = tk.Label(root, text="Turn Score: 0", font=("Arial", 12))
        self.turn_score_label.pack()

        self.total_score_label = tk.Label(root, text="P1: 0 | P2: 0", font=("Arial", 12))
        self.total_score_label.pack(pady=5)

        tk.Button(root, text="🎲 Roll", command=self.roll_dice).pack(pady=5)
        tk.Button(root, text="📥 Hold", command=self.hold).pack(pady=5)
        tk.Button(root, text="🔄 Restart", command=self.reset_game).pack(pady=10)

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.die_label.config(text=f"🎲 Roll: {roll}")

        if roll == 1:
            self.turn_score = 0
            self.switch_player()
        else:
            self.turn_score += roll

        self.update_labels()

    def hold(self):
        self.scores[self.current_player] += self.turn_score
        if self.scores[self.current_player] >= 50:
            messagebox.showinfo("🎉 Winner!", f"Player {self.current_player + 1} wins!")
            self.reset_game()
            return
        self.turn_score = 0
        self.switch_player()
        self.update_labels()

    def switch_player(self):
        self.current_player = 1 - self.current_player
        self.info.config(text=f"Player {self.current_player + 1}'s Turn")

    def update_labels(self):
        self.turn_score_label.config(text=f"Turn Score: {self.turn_score}")
        self.total_score_label.config(text=f"P1: {self.scores[0]} | P2: {self.scores[1]}")

    def reset_game(self):
        self.scores = [0, 0]
        self.turn_score = 0
        self.current_player = 0
        self.info.config(text="Player 1's Turn")
        self.die_label.config(text="🎲 Roll: -")
        self.update_labels()

if __name__ == "__main__":
    root = tk.Tk()
    app = PigGameGUI(root)
    root.mainloop()

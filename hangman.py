import tkinter as tk
from tkinter import messagebox
import random

WORDS = [
    "python", "hangman", "developer", "programming", "interface", "keyboard",
    "language", "software", "hardware", "window", "debug", "function",
    "variable", "exception", "object", "inheritance", "compiler", "binary", "room"
]

MAX_ATTEMPTS = 6

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Hangman Game")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.word = random.choice(WORDS)
        self.display_word = ["_" for _ in self.word]
        self.guessed_letters = set()
        self.attempts_left = MAX_ATTEMPTS

        self.title_label = tk.Label(root, text="Hangman", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.word_label = tk.Label(root, text=" ".join(self.display_word), font=("Courier", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry.pack()
        self.entry.focus()

        self.submit_button = tk.Button(root, text="Guess", command=self.check_letter)
        self.submit_button.pack(pady=10)

        self.status_label = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.guessed_label = tk.Label(root, text="Guessed letters: ", font=("Arial", 12))
        self.guessed_label.pack()

    def check_letter(self):
        guess = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid input", "Please enter a single alphabet.")
            return

        if guess in self.guessed_letters:
            self.status_label.config(text=f"You already guessed '{guess}'.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.display_word[i] = guess
        else:
            self.attempts_left -= 1

        self.update_display()

    def update_display(self):
        self.word_label.config(text=" ".join(self.display_word))
        self.status_label.config(text=f"Attempts left: {self.attempts_left}")
        self.guessed_label.config(text=f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

        if "_" not in self.display_word:
            messagebox.showinfo("You Win!", f"🎉 Congratulations! The word was: {self.word}")
            self.root.destroy()

        elif self.attempts_left == 0:
            messagebox.showerror("Game Over", f"💀 You lost! The word was: {self.word}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()

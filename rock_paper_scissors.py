import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("✊ Rock 🧻 Paper ✂️ Scissors")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        self.label_title = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"))
        self.label_title.pack(pady=10)

        self.result_label = tk.Label(root, text="Make your move!", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        tk.Button(self.button_frame, text="Rock", width=10, command=lambda: self.play("Rock")).grid(row=0, column=0, padx=10)
        tk.Button(self.button_frame, text="Paper", width=10, command=lambda: self.play("Paper")).grid(row=0, column=1, padx=10)
        tk.Button(self.button_frame, text="Scissors", width=10, command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=10)

        # Computer choice display
        self.computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
        self.computer_choice_label.pack(pady=10)

        # Reset button
        tk.Button(root, text="Reset Score", command=self.reset_score).pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        self.computer_choice_label.config(text=f"Computer chose: {computer_choice}")

        result = self.get_result(user_choice, computer_choice)
        self.result_label.config(text=result)

        self.score_label.config(text=f"You: {self.user_score}  |  Computer: {self.computer_score}")

    def get_result(self, user, computer):
        if user == computer:
            return "It's a draw!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):
            self.user_score += 1
            return "✅ You win!"
        else:
            self.computer_score += 1
            return "❌ You lose!"

    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="You: 0  |  Computer: 0")
        self.result_label.config(text="Make your move!")
        self.computer_choice_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

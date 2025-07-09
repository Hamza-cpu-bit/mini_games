import tkinter as tk
from tkinter import messagebox
import random

# Sample data – You can expand this list
capital_data = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Japan": "Tokyo",
    "Canada": "Ottawa",
    "Australia": "Canberra",
    "India": "New Delhi",
    "China": "Beijing",
    "Brazil": "Brasília",
    "Russia": "Moscow",
    "USA": "Washington, D.C.",
    "Egypt": "Cairo",
    "South Africa": "Pretoria",
    "Mexico": "Mexico City",
    "Argentina": "Buenos Aires",
    "Turkey": "Ankara",
    "Saudi Arabia": "Riyadh",
    "South Korea": "Seoul"
}

class CapitalQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("🌍 Capital City Quiz")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.score = 0
        self.question_no = 0
        self.questions = random.sample(list(capital_data.items()), 5)

        self.country_label = tk.Label(root, text="", font=("Arial", 16))
        self.country_label.pack(pady=20)

        self.options = []
        for _ in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=30)
            btn.pack(pady=5)
            self.options.append(btn)

        self.status = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.status.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.question_no >= len(self.questions):
            messagebox.showinfo("Quiz Over", f"🎉 Final Score: {self.score}/{len(self.questions)}")
            self.root.destroy()  # ✅ Close the GUI properly
            return

        country, correct = self.questions[self.question_no]
        self.country_label.config(text=f"What is the capital of {country}?")

        choices = [correct]
        while len(choices) < 4:
            cap = random.choice(list(capital_data.values()))
            if cap not in choices:
                choices.append(cap)
        random.shuffle(choices)

        for i, btn in enumerate(self.options):
            btn.config(text=choices[i], command=lambda b=choices[i]: self.check_answer(b))

    def check_answer(self, selected):
        correct = self.questions[self.question_no][1]
        if selected == correct:
            self.score += 1
        self.question_no += 1
        self.status.config(text=f"Score: {self.score}")
        self.load_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = CapitalQuiz(root)
    root.mainloop()

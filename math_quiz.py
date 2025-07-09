import tkinter as tk
from tkinter import messagebox
import random
import operator

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Timed Math Quiz")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv
        }

        self.score = 0
        self.current_q = 0
        self.total_q = 5
        self.time_limit = 5
        self.timer_id = None

        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=10)

        self.timer_label = tk.Label(root, text="", font=("Arial", 12))
        self.timer_label.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        self.next_question()

    def next_question(self):
        if self.current_q >= self.total_q:
            self.end_quiz()
            return

        self.feedback_label.config(text="")
        self.time_left = self.time_limit
        self.update_timer()

        self.op_symbol, self.op_func = random.choice(list(self.operators.items()))
        self.a = random.randint(1, 20)
        self.b = random.randint(1, 10 if self.op_symbol == '/' else 20)
        self.b = self.b if self.b != 0 else 1

        self.correct_answer = self.op_func(self.a, self.b)
        self.question_label.config(text=f"Q{self.current_q + 1}: What is {self.a} {self.op_symbol} {self.b}?")
        self.entry.delete(0, tk.END)
        self.current_q += 1

    def update_timer(self):
        self.timer_label.config(text=f"⏱ Time left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.feedback_label.config(text=f"⏰ Time's up! Correct: {self.correct_answer}")
            self.root.after(1000, self.next_question)

    def check_answer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        user_input = self.entry.get().strip()
        try:
            if int(user_input) == self.correct_answer:
                self.feedback_label.config(text="✅ Correct!")
                self.score += 1
            else:
                self.feedback_label.config(text=f"❌ Wrong! Correct: {self.correct_answer}")
        except:
            self.feedback_label.config(text=f"⚠️ Invalid input! Correct: {self.correct_answer}")

        self.root.after(1000, self.next_question)

    def end_quiz(self):
        messagebox.showinfo("Quiz Over", f"🎉 Your Score: {self.score} / {self.total_q}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()

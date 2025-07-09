import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Random Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=10)
        self.length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.length_entry.insert(0, "12")
        self.length_entry.pack(pady=5)

        # Options
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Uppercase Letters (A-Z)", variable=self.use_upper).pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Include Lowercase Letters (a-z)", variable=self.use_lower).pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Include Numbers (0-9)", variable=self.use_digits).pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=self.use_symbols).pack(anchor="w", padx=20)

        # Output Field
        self.result_field = tk.Entry(root, font=("Arial", 14), justify="center", width=30)
        self.result_field.pack(pady=15)

        # Buttons
        tk.Button(root, text="Generate Password", command=self.generate_password).pack(pady=5)
        tk.Button(root, text="Copy to Clipboard", command=self.copy_password).pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showwarning("Too Short", "Password length must be at least 4.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        characters = ""
        if self.use_upper.get():
            characters += string.ascii_uppercase
        if self.use_lower.get():
            characters += string.ascii_lowercase
        if self.use_digits.get():
            characters += string.digits
        if self.use_symbols.get():
            characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

        if not characters:
            messagebox.showwarning("No Characters", "Select at least one character set.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_field.delete(0, tk.END)
        self.result_field.insert(0, password)

    def copy_password(self):
        password = self.result_field.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("Empty", "No password to copy.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe ✖️⭕")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 20, "bold")).pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for row in range(3):
            for col in range(3):
                button = tk.Button(self.frame, text="", font=("Arial", 32), width=4, height=1,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        self.status_label = tk.Label(self.root, text="Player X's turn", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled")

            if self.check_winner(self.current_player):
                messagebox.showinfo("🎉 Winner!", f"Player {self.current_player} wins!")
                self.disable_all_buttons()
            elif self.is_draw():
                messagebox.showinfo("Draw", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        # Check rows, columns, diagonals
        return any(
            all(self.board[r][c] == player for c in range(3)) or
            all(self.board[c][r] == player for c in range(3)) for r in range(3)
        ) or all(self.board[i][i] == player for i in range(3)) or \
               all(self.board[i][2 - i] == player for i in range(3))

    def is_draw(self):
        return all(self.board[r][c] != "" for r in range(3) for c in range(3))

    def disable_all_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.status_label.config(text="Player X's turn")
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

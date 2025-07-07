#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:01:21 2025

@author: nazar
"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row): return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2 - i] == player for i in range(3)): return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        try:
            row = int(input(f"{player}'s Turn - Row (0-2): "))
            col = int(input("Col (0-2): "))
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board, player):
                    print_board(board)
                    print(f"{player} wins!")
                    return
                turn += 1
            else:
                print("Cell already taken!")
        except:
            print("Invalid input. Try again.")
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()

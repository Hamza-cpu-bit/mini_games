#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:04:28 2025

@author: nazar
"""

import random

def rps():
    choices = ['rock', 'paper', 'scissors']
    user = input("Choose rock, paper or scissors: ").lower()
    computer = random.choice(choices)
    print(f"Computer chose {computer}")

    if user == computer:
        print("It's a draw!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    rps()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:02:48 2025

@author: nazar
"""

import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 7
    print("Guess the number between 1 and 100!")

    while attempts > 0:
        guess = int(input(f"You have {attempts} attempts: "))
        if guess == number:
            print("🎉 Correct! You win!")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1

    print(f"Out of attempts! The number was {number}")

if __name__ == "__main__":
    guess_number()

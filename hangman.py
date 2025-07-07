#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 11:35:41 2025

@author: nazar
"""

import random

def hangman():
    words = ["python", "banana", "anaconda", "science", "keyboard","city","dubai","hello"]
    word = random.choice(words)
    guessed = set()
    tries = 6

    print("🎮 Let's play Hangman!")

    while tries > 0:
        display = [letter if letter in guessed else "_" for letter in word]
        print("Word:", " ".join(display))

        if "_" not in display:
            print("🎉 You won!")
            return

        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("⚠️ Already guessed.")
        elif guess in word:
            print("✅ Good guess!")
            guessed.add(guess)
        else:
            print("❌ Wrong!")
            guessed.add(guess)
            tries -= 1
            print(f"Tries left: {tries}")

    print(f"💀 You lost. The word was: {word}")

hangman()

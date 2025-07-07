#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:06:12 2025

@author: nazar
"""

import random

capitals = {
    "France": "Paris", "Germany": "Berlin", "Italy": "Rome",
    "India": "New Delhi", "Japan": "Tokyo", "USA": "Washington"
}

def capital_quiz():
    score = 0
    countries = list(capitals.keys())
    random.shuffle(countries)

    for country in countries:
        ans = input(f"What is the capital of {country}? ").strip()
        if ans.lower() == capitals[country].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! It’s {capitals[country]}")
    print(f"Final Score: {score}/{len(countries)}")

if __name__ == "__main__":
    capital_quiz()

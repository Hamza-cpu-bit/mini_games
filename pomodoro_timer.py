#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:11:55 2025

@author: nazar
"""

import time

def countdown(seconds):
    try:
        seconds = int(seconds)
        while seconds:
            mins, secs = divmod(seconds, 60)
            print(f"{mins:02}:{secs:02}", end='\r')
            time.sleep(1)
            seconds -= 1
        print("⏰ Time's up!            ")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    user_input = input("Enter countdown time in seconds: ")
    countdown(user_input)

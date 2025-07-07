#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 11:38:12 2025

@author: nazar
"""

import random
import operator
import signal

# Handle timeout using signal (Unix-based systems only)
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

signal.signal(signal.SIGALRM, timeout_handler)

def timed_math_quiz():
    print("📘 Welcome to the Timed Math Quiz!")
    print("⏱️ You have 5 seconds for each question.\n")

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv
    }

    score = 0

    for i in range(1, 6):
        op_symbol, op_func = random.choice(list(ops.items()))
        a = random.randint(1, 20)
        b = random.randint(1, 10 if op_symbol == '/' else 20)
        if op_symbol == '/' and b == 0:
            b = 1  # Avoid divide by zero

        correct = op_func(a, b)
        question = f"Q{i}: What is {a} {op_symbol} {b}? "

        try:
            signal.alarm(5)  # 5-second timer
            answer = input(question)
            signal.alarm(0)  # Reset timer

            if int(answer) == correct:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {correct}\n")
        except TimeoutException:
            print("\n⏰ Time's up! Moving on.\n")
        except:
            print(f"⚠️ Invalid input. Correct answer: {correct}\n")

    print(f"🎉 Game Over! Your score: {score}/5")

timed_math_quiz()

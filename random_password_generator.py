#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 12:11:13 2025

@author: nazar
"""

import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Password length: "))
    print("🔐 Your password:", generate_password(length))

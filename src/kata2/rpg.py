#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation

    for valor in range(passLen):
        char = random.choice(characters)
        password += char

    return password

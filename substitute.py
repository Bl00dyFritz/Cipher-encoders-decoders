#!/usr/bin/env python3

import getopt, sys
import string
import random

def generate_substitution_table():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    substitution_table = dict(zip(alphabet, shuffled))
    return substitution_table

def encode(text):
    table = generate_substitution_table()
    print (table)
    result = ""
    textU = text.upper()
    for char in textU:
        if char == ' ':
            result += char
        else:
            result += table[char]
    return result

if __name__ == "__main__":
    argList = sys.argv[1:]
    options = "hi:"
    long_options = ["help", "input="]

    text = ""

    try:
        args, vals = getopt.getopt(argList, options, long_options)

        for current_arg, current_val in args:
            if current_arg in ("-h", "--help"):
                print("""help(-h): print this message
                input(-i)[TEXT]: text to be encoded""")
            elif current_arg in ("-i", "--input"):
                text += current_val
    except getopt.error as err:
        print(str(err))

    print("Encrypted: ", encode(text))

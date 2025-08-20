#!/usr/bin/env python3

import getopt, sys

qwerty_map = {
        'Q': 'W', 'W': 'E', 'E': 'R', 'R': 'T', 'T': 'Y', 'Y': 'U', 'U': 'I', 'I': 'O', 'O': 'P', 'P': 'Q',
        'A': 'S', 'S': 'D', 'D': 'F', 'F': 'G', 'G': 'H', 'H': 'J', 'J': 'K', 'K': 'L', 'L': 'A',
        'Z': 'X', 'X': 'C', 'C': 'V', 'V': 'B', 'B': 'N', 'N': 'M', 'M': 'Z',
        ' ': ' '
    }

def encode(text):
    result = ""
    textU = text.upper()
    for char in textU:
        result += qwerty_map[char]
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

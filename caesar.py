#!/usr/bin/env python3

import getopt, sys

def encode(text, shift):
    result = ""
    textU = text.upper()
    for char in textU:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

if __name__ == "__main__":
    argList = sys.argv[1:]
    options = "hi:s:"
    long_options = ["help", "input=", "shift="]

    text = ""
    shift = 0

    try:
        args, vals = getopt.getopt(argList, options, long_options)

        for current_arg, current_val in args:
            if current_arg in ("-h", "--help"):
                print("""help(-h): prints this message
                input(-i)[TEXT]: text to be encoded
                shift(-s)[VAL]: number of spaces to shift""")
            elif current_arg in ("-i", "--input"):
                text += current_val
            elif current_arg in ("-s", "--shift"):
                shift = int(current_val)
    except getopt.error as err:
        print(str(err))

    print("Encrypted: ", encode(text, shift))

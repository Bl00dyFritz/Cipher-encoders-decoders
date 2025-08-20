#!/usr/bin/env python3

import getopt, sys

def encode(text, key):
    result = ""
    keypos = 0
    keyU = key.upper()
    textU = text.upper()

    for char in textU:
        if char.isupper():
            result += chr((ord(char) - ord('A') + (ord(keyU[keypos]) - ord('A'))) % 26 + ord('A'))
            keypos = (keypos + 1) % len(key)
        else:
            result += char
    return result

if __name__ == "__main__":
    argList = sys.argv[1:]
    options = "hi:k:"
    long_options = ["help", "input=", "key="]

    text = ""
    key = ""

    try:
        args, vals = getopt.getopt(argList, options, long_options)

        for current_arg, current_val in args:
            if current_arg in ("-h", "--help"):
                print("""help(-h): prints this message
                input(-i)[TEXT]: text to be encoded
                key(-k)[TEXT]: the key string""")
            elif current_arg in ("-i", "--input"):
                text += current_val
            elif current_arg in ("-k", "--key"):
                key += current_val
    except getopt.error as err:
        print(str(err))

    print("Encrypted: ", encode(text, key))

#!/usr/bin/env python3

import getopt, sys

def encode(text):
    result = "".join(format(ord(char), '08b') for char in text)
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

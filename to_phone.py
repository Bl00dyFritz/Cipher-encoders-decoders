#!/usr/bin/env python3

import getopt, sys

phone_map = {    
        'A': '2',    'B': '22',   'C': '222',
        'D': '3',    'E': '33',   'F': '333',
        'G': '4',    'H': '44',   'I': '444',
        'J': '5',    'K': '55',   'L': '555',
        'M': '6',    'N': '66',   'O': '666',
        'P': '7',    'Q': '77',   'R': '777', 'S': '7777',
        'T': '8',    'U': '88',   'V': '888',
        'W': '9',    'X': '99',   'Y': '999', 'Z': '9999',
        ' ': '0'
    }

def encode(text):
    result = ""
    textU = text.upper()
    for char in textU:
        result += phone_map[char]
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

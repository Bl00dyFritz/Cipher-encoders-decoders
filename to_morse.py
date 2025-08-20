#!/usr/bin/env python3

import getopt, sys

morse_dict = {
        'A': '.-',    'B': '-...',  'C': '-.-.',
        'D': '-..',   'E': '.',     'F': '..-.',
        'G': '--.',   'H': '....',  'I': '..',
        'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',
        'S': '...',   'T': '-',     'U': '..-',
        'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        ' ': '/'
    }

def encode(text):
    result = ""
    textU = text.upper()
    for char in textU:
        result += morse_dict[char]
        result += ' '
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

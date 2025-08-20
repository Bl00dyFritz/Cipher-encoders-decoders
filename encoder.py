#!/usr/bin/env/ python3
import string
import random

word = "HELLO WORLD"
key = "DUCK"

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

qwerty_map = {
        'Q': 'W', 'W': 'E', 'E': 'R', 'R': 'T', 'T': 'Y', 'Y': 'U', 'U': 'I', 'I': 'O', 'O': 'P', 'P': 'Q',
        'A': 'S', 'S': 'D', 'D': 'F', 'F': 'G', 'G': 'H', 'H': 'J', 'J': 'K', 'K': 'L', 'L': 'A',
        'Z': 'X', 'X': 'C', 'C': 'V', 'V': 'B', 'B': 'N', 'N': 'M', 'M': 'Z',
        ' ': ' '
    }

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

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift + 1) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift + 1) % 26 + ord('a'))
        else:
            result += char
    return result

def key_shift(text, key):
    result = ""
    keypos = 0
    keyU = key.upper()
    keyL = key.lower()
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + (ord(keyU[keypos]) - ord('A') + 1)) % 26 + ord('A'))
            keypos = (keypos + 1) % len(key)
        elif char.islower():
            result += chr((ord(char) - ord('a') + (ord(keyL[keypos]) - ord('a') + 1)) % 26 + ord('a'))
            keypos = (keypos + 1) % len(key)
        else:
            result += char
    return result

def to_binary(text):
    result = "".join(format(ord(char), '08b') for char in text)
    return result

def to_hex(text):
    bytes_data = text.encode("utf-8")
    return bytes_data.hex()

def to_phone(text):
    result = ""
    textU = text.upper()
    for char in textU:
        result += phone_map[char]
    return result

def qwerty_shift(text):
    result = ""
    textU = text.upper()
    for char in textU:
        result += qwerty_map[char]
    return result

def to_morse(text):
    result = ""
    textU = text.upper()
    for char in textU:
        result += morse_dict[char]
        result += ' '
    return result

def generate_substitution_table():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    substitution_table = dict(zip(alphabet, shuffled))
    return substitution_table

def substitution_cipher(text):
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

# Example usage:
if __name__ == "__main__":
    for i in range(26):
        encrypted = caesar_cipher(word, i)
        print("Encrypted:", encrypted)
    print ("Key shift: ", key_shift(word, key), "Key: ", key)
    print ("Binary: ", to_binary(word))
    print ("Hex: ", to_hex(word))
    print ("Phone: ", to_phone(word))
    print ("QWERTY shift: ", qwerty_shift(word))
    print ("Morse code: ", to_morse(word))
    print ("Substitution: ", substitution_cipher(word))

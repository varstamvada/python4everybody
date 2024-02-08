# caesar.py
import string

def shift_n(letter, amount):
    if letter not in string.ascii_lowercase:
        return letter
    new_letter = ord(letter) + amount
    while new_letter > ord("z"):
        new_letter -= 26
    while new_letter < ord("a"):
        new_letter += 26
    return chr(new_letter)

def caesar(message, amount):
    enc_list = [shift_n(letter, amount) for letter in message]
    return "".join(enc_list)
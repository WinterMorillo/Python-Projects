"""
    Welcome to the Caesar Cipher program!

    If you want to encrypt your message, so anybody can actually get a hold of the information,
    this is the right program for you.

    Steps:

    Enter either encode or decode.
        Encode: To hide the information using the Caesar Cipher method.
        Decode: To reveal the information using the Caesar Cipher method.
    Enter the message to encode.
    Enter the shift amount of the message.
    Copy the encoded message with the person you want.
"""

import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    cipher_text = ""
    for i in text:
        if i in alphabet:
            x = text.index(i)
            y = alphabet.index(text[x])
            if y + shift >= 26:
                y = 0 - 1
                cipher_text += alphabet[y + shift]
            else:
                y = alphabet.index(text[x])
                cipher_text += alphabet[y + shift]
        else:
            cipher_text += i

    print(f"The encrypted message is {cipher_text}")


def decrypt(text, shift):
    cipher_text = ""
    for i in text:
        if i in alphabet:
            x = text.index(i)
            y = alphabet.index(text[x])
            if y + shift >= 26:
                y = 0 + 1
                cipher_text += alphabet[y - shift]
            else:
                cipher_text += alphabet[y - shift]
        else:
            cipher_text += i

    print(f"The decrypted message is {cipher_text}")


close_program = False
while not close_program:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to     decrypt:\nif     "
        "you want to close the program, enter \"close\"\n").lower()

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        decrypt(text, shift)
    elif direction == "close":
        close_program = True
    else:
        print(f"You entered {direction}, this option is invalid, please try again!")

if close_program:
    print("Thank you for participating")


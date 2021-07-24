from art import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, direction):
    final_text = ''
    encode = True

    for letter in plain_text:
        if letter not in alphabet:
            final_text += letter
        elif direction == 'encode':
            position = alphabet.index(letter)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        elif direction == 'decode':
            position = alphabet.index(letter)+26
            new_position = position - shift_amount
            final_text += alphabet[new_position]   

    print(f"The {direction} text is {final_text}")

print(logo)

continue_program = 'yes'

while continue_program != 'no':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift, direction=direction)

    continue_program = input("Type 'yes' if you want to go again. Otherwise type 'no. ")
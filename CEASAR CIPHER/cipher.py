import cipher_art
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(cipher_art.logo)

def cipher(message, shift, process):
    container = ""
    if process == "d":
        shift = -shift  # Corrected to subtract the shift for decoding
    for letter in message:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            new_index = (old_index + shift) % len(alphabet)
            ciphered = alphabet[new_index]
            container += ciphered
        else:
            container += letter

    return container

condition = True
while condition:
    process = input("What process do you want to execute?\n[d] Decode   [e] Encode\n:").lower()
    message = input("Enter your message\n:")
    shift = int(input("Shift number\n:"))
    
    result = cipher(message, shift, process)
    print(result)

    decision = input("Do you want to repeat the process?\n[y] Yes   [n] No\n:").lower()
    if decision == "n":
        condition = False
    elif decision != "y":
        print("\n...")

clear()

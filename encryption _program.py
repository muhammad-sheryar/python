#Python Encrytpion Program

import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(char)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"{key}")


#Encryption

plain_text = input("Enter a message to Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"Original Message: {plain_text}")
print(f"Encryted Message: {cipher_text }")

#Decryption

cipher_text_text = input("Enter a message to Decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f"Encryted Message: {cipher_text }")
print(f"Original Message: {plain_text}")
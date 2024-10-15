import random
import string

chars = (" ") + string.punctuation+ string.digits + string.ascii_letters #this will give us a bunch of letters
chars = list(chars) # this will turn them from a big string to a list of each string
key = chars.copy() # this for the encryption

random.shuffle(key) #this randomize our key

#ENCRYPT
plain_text = input("Enter a message to encypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")


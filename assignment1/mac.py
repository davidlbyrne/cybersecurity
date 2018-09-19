"""
Michael Soltys
Mono-Alphabetic Cipher (MAC) Implementation
Two types of keys: Caesar and Permutation
Created: June 3, 2017
Updated: June 6, 2017 (corrections from Nick Stern)
"""

import sys
import base64
import binascii
import numpy as np
import pdb

base64alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
'P','Q','R','S','T','U','V','W','X','Y','Z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z',
'0','1','2','3','4','5','6','7','8','9','+','/']

def encode_base64(fileName):
    plaintext_file = open(fileName,'rb')
    plaintext = plaintext_file.read()
    encoded = base64.b64encode(plaintext)

    encoded_string = ""
    for character_value in encoded:
        encoded_string += chr(ord(character_value))
    return encoded_string

def decode_base64(fileName):
    plaintext_file = open(fileName,'r')
    plaintext_base64 = plaintext_file.read()
    decoded = base64.b64decode(plaintext_base64)
    decoded_string = ""
    for character_value in decoded:
        decoded_string += chr(ord(character_value))
    return decoded_string
 
def encrypt_caesar(plaintext_base64,offset):
    ciphertext_base64 = ''
    for character in plaintext_base64:
        if (character != '='):
            alphabet_index = base64alphabet.index(character)
            ciphertext_base64 += base64alphabet[(alphabet_index+offset) % 64]
        else:
            ciphertext_base64 += '='
    return ciphertext_base64
 
def encrypt_mac(plaintext_base64,permutation):
    ciphertext_base64 = ""
    for character in plaintext_base64:
        if (character != '='):
            alphabet_index = base64alphabet.index(character)
            perm_index = permutation[alphabet_index]
            ciphertext_base64 += base64alphabet[perm_index]
        else:
            ciphertext_base64 += '='
    return ciphertext_base64
 
if __name__ == "__main__":
    # run as follows: python3 mac.py <filename> [caesar|mac] [key_shift]
    # where the key_shift is only required for caesar encryption
    # because mac encryption will generate a random permutation: key_perm
    if (sys.argv[2] == "caesar"):
        key_shift = int(sys.argv[3])
        print("Key=",key_shift)
        output = encrypt_caesar(encode_base64(sys.argv[1]),key_shift)
    elif (sys.argv[2] == "mac"):
        key_perm = np.random.permutation(64)
        print("Key=",key_perm)
        output = encrypt_mac(encode_base64(sys.argv[1]),key_perm)
    # display: if short ciphertext (<=70 characters), display in one line 
		# if long ciphertext (>70 characters) display in lines of 50
    # characters (except possibly, for the last line)
    print("Base 64 Encrypted String: ")
    if (len(output)>70):
        outputString = ""
        for c in range(len(output)):
            if (c % 50 == 0 and c != 0):
                outputString += "\n"    
            outputString += output[c]
        print(outputString)
    else:
        print(output)

import numpy as np
import sys
base64alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
'P','Q','R','S','T','U','V','W','X','Y','Z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z',
'0','1','2','3','4','5','6','7','8','9','+','/']



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

key_perm = np.random.permutation(64)
print("Key=",key_perm)
output = encrypt_mac(sys.argv[1],key_perm)
print(output)







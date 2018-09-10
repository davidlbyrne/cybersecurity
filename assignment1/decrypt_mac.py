import sys
import itertools
import base64
import binascii
import numpy as np

my_dict=['and','when','if','where','the']
base64alphabet=[ 'A', 'B', 'C', 'D' , 'E', 'F', 'G' , 'H','I','J', 'K' , 'L', 'M' , 'N', 'O' ,'P', 'Q' , 'R','S', 'T', 'U', 'V', 'W' , 'X', 'Y', 'Z',
'a','b','c','d','e','f','g','h','i','j','k','l', 'm' ,'n','o',' p','q','r','s','t','u','v', 'w','x','y','z',
'0','1','2','3','4','5','6','7','8','9', '+' ,'/']
def decode_base64(decrypt_msg):
    decoded = base64.b64decode(decrypt_msg)
    decoded_string = ""
    for character_value in decoded:
        decoded_string += chr(character_value)
    return decoded_string

def check_words(plain_text,my_dict):
      score = 0 
      for word in dict:  
       if word in plain_text:
         score = score +1
       if score > 1: return true  


def bruteforce_mac(base64alphabet,ciphertext):
  n=[]
  for i in range(64) : 
      n.append(i)
  print("n",n)
  #All possible keys 
  combos=itertools.permutations(n)
  decrypt_msg=""
  for key in combos: 
    for letter in ciphertext:
      print(key)
      print("len :",len(base64alphabet))
      print("letter :",letter)
      i = base64alphabet.index(letter)
      j = key.index(i)
      decrypt_msg += base64alphabet[j]
      plaintext= decode_base64(decrypt_msg)
    if check_words(plaintext,my_dict): return(key,plaintext)


#Entry point

fileName=sys.argv[1]
plaintext_file = open(fileName,'rb')
ciphertext = plaintext_file.read()
key,plaintext = bruteforce_mac(base64alphabet,ciphertext)
print("key :",key)
print("plaintext :", plaintext)


# APLHA = "A B C D" 
#  key = "2 1 3 0"

# txt = CAB

# DCB


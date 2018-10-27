# Assignment2 - Assignment 2, due November 7, 2018: Problem 6.1 in the lecture notes. You may import the following packages from Python libraries:

import sys
from Crypto.Cipher import DES
from Crypto import Random


#setup and validate input 
# Set up key , plain text , cipher text , and IV
key = sys.argv[1]
file = open(sys.argv[2] , ” r ” )
plaintext=file.read()
file.close()
ciphertext = ””
iv = Random.new().read(DES.blocksize)

#helper function to transform bas64 key to bin
#KavahRihanDavid

#xor function	

#Encrypt function
des_cbc_encrypt() :  
#des first round 
    obj = DES.new(key,DES.MODE_CBC) 
    pte = check pad (plaintext[:8])
    plaintext = plaintext[8:]
    pte = xor(pte,iv)
    previous = obj.encrypt(pte) 
    ciphertext = ciphertext + obj.encrypt(pte)
    # begin remaining rounds
    for i in range (0,(len(plaintext)/8) − ord (chr( not bool(len(plaintext)%8))) + 1) : 
        pte = check pad (plaintext[ : 8 ] )
        plaintext = plaintext[ 8 : ]
        pte = xor (pte,previous)
        previous = obj.encrypt(pte)
        ciphertext = ciphertext + obj.encrypt(pte) # add on to c i p h e r t e x t

#Decrypt Function 
#des first round 
#remaining rounds 


#print 





'''
$ more test.txt 
Hello, World!
$ python des-cbc.py 12345678 test.txt | xxd -b
00000000: 11100000 01011001 00110010 11110100 00101101 10100110  .Y2.-.
00000006: 11111011 01101011 00001000 00100001 10011100 01011100  .k.!.\
0000000c: 11000111 10110010 11001000 01001010 00001010           ...J.

'''





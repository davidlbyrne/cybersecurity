# Assignment2 - Assignment 2, due November 7, 2018: Problem 6.1
# in the lecture notes. You may import the following packages from
# Python libraries:

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

def checkpad(plaintext):
    lenght= len(plaintext)
    rem = length%8
    # Pad indicates how many characters we have to add to the end of the file
    pad = 8 - rem
    # the first meaningless number in binary is (10000000) which is equal to 128
    z= 128
    for i in range (pad):
        plaintext= plaintext + chr (z + pad)
    return (plaintext)



# xor function
def xor(lft, rht):
    # set up 8 char arrays with none elements
    lft_ba = [None] * 8
    rht_ba = [None] * 8

    # step through each letter and conv to integer and store
    for i in range(0, 8):
        lft_ba[i] = ord(lft[i])
        rht_ba[i] = ord(rht[i])

    # finally the result of xor
    xor_res = [None] * 8
    for i in range(0, 8):
        xor_res[i] = lft_ba[i] ^ rht_ba[i]

    # convert the bits into char again
    char_xor = ''
    for k in xor_res:
        char_xor.join(chr(k))

    return char_xor

#Encrypt function
des_cbc_encrypt(plaintext,key) :
    #des first round 
    obj = DES.new(key,DES.MODE_CBC) 
    plaintext = checkpad(plaintext)
    pte = plaintext[:8]
    plaintext = plaintext[8:]
    pte = xor(pte,iv)
    previous = obj.encrypt(pte) 
    ciphertext = ciphertext + obj.encrypt(pte)
    # begin remaining rounds
    for i in range (0,(len(plaintext)/8)) : 
        pte = checkpad(plaintext[:8])
        plaintext = plaintext[8:]
        pte = xor(pte,previous)
        previous = obj.encrypt(pte)
        ciphertext=ciphertext+obj.encrypt(pte)
    return ciphertext
#Decrypt Function 
#des first round 
#remaining rounds 


#print 
=======
        ciphertext = ciphertext + obj.encrypt(pte) # add on to c i p h e r t e x t

# remaining rounds
>>>>>>> feature/decrypt_dec

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

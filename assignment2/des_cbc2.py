#!/usr/local/bin/python3
# Assignment2 - Assignment 2, due November 7, 2018: Problem 6.1
# in the lecture notes. You may import the following packages from
# Python libraries:

import sys
import os
import binascii
from Crypto.Cipher import DES
from Crypto import Random



def checkpad(plaintext):
    length= len(plaintext)
    if ((length % 8) != 0):
        rem = length%8
        # Pad indicates how many characters we have to add to the end of the file
        pad = 8 - rem
        # the first meaningless number in binary is (10000000) which is equal to 128
        for i in range (pad):
            plaintext= plaintext + chr (0)
    return (plaintext)


# xor function
def xor(lft, rht):
    # set up 8 char arrays with none elements
    lft_ba = [None,None,None,None,None,None,None,None]
    rht_ba = [None]*8
    # print(lft_ba)
    # print(lft, rht)
    # step through each letter and conv to integer and store
    for i in range(0,8):
        # print(i)
        lft_ba[i] = ord(lft[i])
        rht_ba[i] = ord(rht[i])
    # finally the result of xor
    xor_res = [None] * 8
    for i in range(0, 8):
        xor_res[i] = lft_ba[i] ^ rht_ba[i]
    # convert the bits into char again
    ret=""
    # print('xor_result:',xor_res)
    return bytes(bytearray(xor_res))

#Encrypt function
def des_cbc_encrypt(plaintext,key,iv) :
    ciphertext=b''
    previous=""
    #des first round 
    obj = DES.new(key,DES.MODE_ECB) 
    plaintext = checkpad(plaintext)
    pte = plaintext[:8]
    plaintext = plaintext[8:]
    # print("pte:",pte)
    pte = xor(iv,pte)
    # print(len(pte))
    previous = obj.encrypt(pte)
    # print(len(previous), previous)
    ciphertext = ciphertext + previous
    # begin remaining rounds
    for i in range (0,int((len(plaintext)/8))) : 
        pte = checkpad(plaintext[:8])
        plaintext = plaintext[8:]
        # print("encrypting ",len(pte),"bytes :\'",pte,"\'") 
        previous = ''.join([chr(s) for s in bytearray(previous)])
        # print("previous :",previous)
        pte = xor(previous,pte)
        # print(pte,"END")
        # print(len(pte), "pte",pte)
        previous =  obj.encrypt(pte)
        # print(len(previous), previous)
        ciphertext = ciphertext + previous        
    return ciphertext
#Decrypt Function 
#des first round 
#remaining rounds 


if __name__ == '__main__':
    key = sys.argv[1]
    # print("Encrypting :",sys.argv[2])
    file = open(sys.argv[2],'r')
    plaintext=file.read()
    file.close()
    iv = '00000000'
    ciphertext=des_cbc_encrypt(plaintext,key,iv)
    os.write(1,bytes(ciphertext)) 
#print 


'''
$ more test.txt
Hello, World!
$ python des-cbc.py 12345678 test.txt | xxd -b
00000000: 11100000 01011001 00110010 11110100 00101101 10100110  .Y2.-.
00000006: 11111011 01101011 00001000 00100001 10011100 01011100  .k.!.\
0000000c: 11000111 10110010 11001000 01001010 00001010           ...J.
'''

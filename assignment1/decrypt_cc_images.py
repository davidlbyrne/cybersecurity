#! /usr/bin/python3

import mac
import os
import base64


def decrypt_cc_images():
    f = open("assignment-1-c-enc.txt", "r")
    f.readline()
    encrypted_base64_img_string = f.read()

    for guess_offset in range(1, 64):
        base64_string = ""
        for character in encrypted_base64_img_string:
            if ((character != '=') and (character != '\n')):
                alphabet_index = mac.base64alphabet.index(character)
                base64_string += mac.base64alphabet[(alphabet_index -
                                                     guess_offset) % 64]
            elif (character == '\n'):
                base64_string += '\n'
            else:
                base64_string += '='

        temp_filename = "img_offset_" + str(guess_offset) + ".png"

        print('file %s written to disk'.format(temp_filename))
        img2disk = open(os.path.join("cc_base64_images", temp_filename),
                        "wb")
        img2disk.write(base64.b64decode(base64_string))
        img2disk.close()


decrypt_cc_images()

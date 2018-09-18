import mac
import base64
import time

base64_string = ""
alpha = mac.base64alphabet
perm_key = '2JzvLTdIARK3nyDg9s0NhxjGf18YQrk/ei6ZM+ObWCqotaclw7FE5BXHV4puUmPS'
decrypted_txt = ""


def conv_alpha_to_perm_array():
    temp = []
    for char in perm_key:
        index = alpha.index(char)
        temp.append(index)

    return temp


alpha_to_perm_mapping = conv_alpha_to_perm_array()


def decrypt_mac_to_base64_data():
    global decrypted_txt
    f = open("assignment-1-d-enc-clean.txt", "r")
    enc_base64_img_str = f.read()

    for char in enc_base64_img_str:
        print('char at ', char)
        if ((char != '=') and (char != '\n')):
            alpha_index = alpha.index(char)
            if (alpha_index not in alpha_to_perm_mapping):
                print('skipping, alpha_index not found, ', alpha_index)
                continue
            else:
                perm_index = alpha_to_perm_mapping.index(alpha_index)
                char_at_alpha_index = alpha[perm_index]
                decrypted_txt += char_at_alpha_index
        elif (char == '\n'):
            decrypted_txt += '\n'
        else:
            decrypted_txt += '='

    return decrypted_txt


def save_mac_decipher():
    dec_txt = decrypt_mac_to_base64_data()
    img2disk = open('mac_img.png', "wb")
    img2disk.write(base64.b64decode(dec_txt))
    img2disk.close()

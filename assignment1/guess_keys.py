import mac
import numpy as np


str_key = []
our_key = "******M******X***W**I2*jbU/YZS5*eF**8V36z**P*RO**Axe************"

our_key_perm = []

def compute_perm_key_on_our_key():


def build_keys():
    global str_key

    while True:
        key_perm = np.random.permutation(64)
        temp_str_key = ""

        for elm in key_perm:
            temp_str_key += mac.base64alphabet[elm]

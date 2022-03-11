#! /usr/bin/python
# Usage: ./one_time_pad+cipher.py --img /path/to/img
# Maintainer: robotastray

from typing import Tuple 
import base64
from secrets import token_bytes
import argparse
import imghdr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original_str: str) -> Tuple[int, int]:
    dummy: int = random_key(len(original_str))
    original_key: int = int.from_bytes(original_str, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7)//8, "big")
    return temp.decode()

def image_to_string(img) -> str:
    with open(img, "rb") as image_string:
         image_str = base64.b64encode(image_string.read())
    return image_str

def string_to_image(image_str: str, img_type: str):
    decodedimg = open("decoded image."+img_type, 'wb')
    decodedimg.write(base64.b64decode(image_str))
    decodedimg.close
    return decodedimg
 
def check_image_type(image) -> str:
    img_type = imghdr.what(image)
    return img_type

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-path",action="store", dest="img",help="path to image")
    output = parser.parse_args()
    original_str = image_to_string(output.img)
    key1, key2 = encrypt(original_str)
    result: str = decrypt(key1, key2)
    img_type = check_image_type(output.img)
    print(img_type)
    string_to_image(result, img_type)
    img = mpimg.imread("decoded image."+img_type)
    imgplot = plt.imshow(img)
    plt.show()




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

def encrypt(original_base64: str) -> Tuple[int, int]:
    dummy: int = random_key(len(original_base64))
    original_key: int = int.from_bytes(original_base64, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7)//8, "big")
    return temp.decode()

def image_to_base64(img) -> str:
    with open(img, "rb") as image_string:
         image_base64 = base64.b64encode(image_string.read())
    return image_base64

def base64_to_image(image_base64: str, img_type: str):
    decodedimg = open("decoded image."+img_type, 'wb')
    decodedimg.write(base64.b64decode(image_base64))
    decodedimg.close
    return decodedimg
 
def check_image_type(image) -> str:
    img_type = imghdr.what(image)
    return img_type

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-path",action="store", dest="img",help="path to image")
    output = parser.parse_args()
    bytes_img = image_to_base64(output.img)
    key1, key2 = encrypt(bytes_img)
    result: str = decrypt(key1, key2)
    img_type = check_image_type(output.img)
    print(img_type)
    base64_to_image(result, img_type)
    #display the image
    img = mpimg.imread("decoded image."+img_type)
    imgplot = plt.imshow(img)
    plt.show()




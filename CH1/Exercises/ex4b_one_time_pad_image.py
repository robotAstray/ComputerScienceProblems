#! /usr/bin/python
# Usage: ./one_time_pad+cipher.py --img /path/to/img
# Maintainer: robotastray
#Copyright: robotAstray (c)
import argparse
import base64
from typing import Tuple
from secrets import token_bytes
import imghdr
import matplotlib.image as mp
import matplotlib.pyplot as plt

def base64_to_image(image_base64: str, img_type: str):
    """Convert from base64 to image"""
    decodedimg = open("decoded image."+img_type, 'wb')
    decodedimg.write(base64.b64decode(image_base64))
    decodedimg.close()

def check_image_type(image) -> str:
    """Check image type (e.g. .png .jpeg)"""
    img_type = imghdr.what(image)
    return img_type 


def decrypt(key1: int, key2: int) -> str:
    """Decrypt data using XOR operation"""
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7)//8, "big")
    return temp.decode()


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original_base64: str) -> Tuple[int, int]:
    """Encrypt data using XOR operation"""
    dummy: int = random_key(len(original_base64))
    original_key: int = int.from_bytes(original_base64, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def image_to_base64(img) -> str:
    """Convert image to base64"""
    with open(img, "rb") as image_string:
        image_base64 = base64.b64encode(image_string.read())
    return image_base64

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", action="store", dest="img", help="path to image")
    output = parser.parse_args()
    # Convert from image to base64
    bytes_img = image_to_base64(output.img)
    # encrypt using XOR operation
    key1, key2 = encrypt(bytes_img)
    # decrypt using XOR operation
    result: str = decrypt(key1, key2)
    # check image type (e.g. .png, .jpeg)
    img_type = check_image_type(output.img)
    print(img_type)
    #convert base64 to image
    base64_to_image(result, img_type)
    # plot/display image
    img = mp.imread("decoded image."+img_type)
    imgplot = plt.imshow(img)
    plt.show()
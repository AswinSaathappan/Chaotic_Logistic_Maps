import cv2
import numpy as np
from chaotic_map import logistic_map
from utils import generate_permutation

def encrypt_image(image_path, x0, r):

    img = cv2.imread(image_path,0)

    flat = img.flatten()

    size = len(flat)

    chaos = logistic_map(x0,r,size)

    perm = generate_permutation(chaos)

    scrambled = flat[perm]

    key = (chaos * 255).astype(np.uint8)

    encrypted = np.bitwise_xor(scrambled,key)

    enc_img = encrypted.reshape(img.shape)

    cv2.imwrite("encrypted.png",enc_img)

    return "encrypted.png"

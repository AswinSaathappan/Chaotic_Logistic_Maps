import cv2
import numpy as np
from chaotic_map import logistic_map
from utils import generate_permutation, inverse_permutation

def decrypt_image(image_path, x0, r):

    img = cv2.imread(image_path,0)

    flat = img.flatten()

    size = len(flat)

    chaos = logistic_map(x0,r,size)

    perm = generate_permutation(chaos)

    inv_perm = inverse_permutation(perm)

    key = (chaos * 255).astype(np.uint8)

    scrambled = np.bitwise_xor(flat,key)

    original = scrambled[inv_perm]

    dec_img = original.reshape(img.shape)

    cv2.imwrite("decrypted.png",dec_img)

    return "decrypted.png"

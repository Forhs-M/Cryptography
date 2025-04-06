import hashlib
from Crypto.Random import get_random_bytes
import random

# bit_flip: Flips a bit from a byte string
# byte_data: The byte string whose bit will get flipped
# bit index: Indicates which bit will get flipped from the byte string
# Returns the byte list with one bit flipped

def bit_flip(byte_data, bit_index):
    byte_list = list(byte_data)
    byte_pos = bit_index // 8
    bit_pos = bit_index % 8
    byte_list[byte_pos] ^= 1 << bit_pos
    return bytes(byte_list)

# bit_collisions: Calculates the number of same bits for 2 given byte strings
# b1: 1st byte string
# b2: 2nd byte string
# Returns the number of same bits in the 2 given byte strings

def bit_collisions(b1, b2):
    collisions = 0
    bits1 = ''.join(format(byte, '08b') for byte in b1)
    bits2 = ''.join(format(byte, '08b') for byte in b2)
    for i in range (len(bits1)):
        if bits1[i] == bits2[i]:
            collisions += 1
    return collisions


# AvallanceCheck_EBC: Check if the avallance effect is present in ECB mode
# Returns True if the avallance effect is observed otherwise returns False

def AvallanceCheck():
    aval = 0
    for i in range(100):
        collisions = 0
        m1 = get_random_bytes(64)
        m2 = bit_flip(m1, random.randint(0, 511))
        c1 = hashlib.sha256(m1).digest()
        c2 = hashlib.sha256(m2).digest()
        collisions = bit_collisions(c1, c2)
        if collisions <= 256:
            aval += 1
    return aval > 50


# Example of using the Check functions

Aval_Check = AvallanceCheck()

print("Avalanche check for SHA 256 results in: ", Aval_Check)    


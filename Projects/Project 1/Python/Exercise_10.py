from Crypto.Cipher import AES
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

def AvallanceCheck_ECB():
    aval = 0
    for i in range(60):
        collisions = 0
        m1 = get_random_bytes(32)
        m2 = bit_flip(m1, random.randint(0, 255))
        key = get_random_bytes(16)
        encrypter = AES.new(key, AES.MODE_ECB)
        c1 = encrypter.encrypt(m1)
        c2 = encrypter.encrypt(m2)
        collisions = bit_collisions(c1, c2)
        if collisions < 128:
            aval += 1
    return aval > 30

# AvalancheCheck_CBC: Checks if the avalanche effect is present in CBC mode
# Returns True if the avallance effect is observed otherwise returns False

def AvalancheCheck_CBC():
    aval = 0
    avg_colls = 0
    for i in range(60):
        m1 = get_random_bytes(32)
        m2 = bit_flip(m1, random.randint(0, 255))
        key = get_random_bytes(16)
        iv = get_random_bytes(16)
        encrypter = AES.new(key, AES.MODE_CBC, iv)
        c1 = encrypter.encrypt(m1)
        encrypter2 = AES.new(key, AES.MODE_CBC, iv)
        c2 = encrypter2.encrypt(m2)
        collisions = bit_collisions(c1, c2)
        avg_colls += collisions
        if collisions < 128:
            aval += 1
    print("Average colls in CBC mode:", avg_colls/60)
    return aval > 30

# Example of using the Check functions

ECB_Check = AvallanceCheck_ECB()
CBC_Check = AvalancheCheck_CBC()

print("Avalanche check for ECB mode results in: ", ECB_Check)    
print("Avalanche check for CBC mode results in: ", CBC_Check) 
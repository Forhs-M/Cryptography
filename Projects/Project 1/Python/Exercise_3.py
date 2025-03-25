# circ_shift_lelft : Performs a circular left shift on a 16 bit message. 
# mess : 16 bit message.
# shift : Number of positions every bit will circular left shift
# Returns the result of circularly shifting 'mess' left by 'shift' bits.

def circ_left_shift (mess, shift):
    shift %= 16
    return((mess << shift) | (mess >> (16 - shift))) & 0b1111111111111111

# encryption : Encrypts a 16 bit message with the encryption method given on excersice 3. 
# mess : 16 bit message that is going to get encrypted.
# Returns the message encrypted.

def encryption (mess):
    mess_6 = circ_left_shift(mess, 6)
    mess_10 = circ_left_shift(mess, 10)
    return mess ^ mess_6 ^ mess_10

# decryption : Decrypts a message encrypted by 'encryption' function.
# enc_mess : Encypted 16 bit message.
# Returns the message decrypted.

def decryption(enc_mess):
    enc_mess_2 = circ_left_shift(enc_mess, 2)
    enc_mess_4 = circ_left_shift(enc_mess, 4)
    enc_mess_12 = circ_left_shift(enc_mess, 12)
    enc_mess_14 = circ_left_shift(enc_mess, 14)
    return enc_mess ^ enc_mess_2 ^ enc_mess_4 ^ enc_mess_12 ^ enc_mess_14

# Example usage of encryption and decryption 
    
mess = 0b1011001111111011
enc_mess = encryption(mess)
dec_mess = decryption(enc_mess)
print(f"Mess = {bin(mess)}")
print(f"Encr = {bin(enc_mess)}")
print(f"Decrypted = {bin(dec_mess)}")
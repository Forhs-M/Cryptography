import random 

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?()-"

# encode : Encodes the given message according to Table 1 from tex. 
# mess : String message to be encoded.
# Returns a list of 5-bit binary strings representing the encoded message.

def encode (mess):
    enc_mess = []
    for char in mess:
        num = alphabet.index(char)
        enc_mess.append(format(num, "05b"))
    return enc_mess

# decode : Decodes a list of 5-bit binary stirngs given message according to table 1 from tex.
# enc_mess : A list of binary strings to be decoded.
# Returns the decoded message in Latin characters.

def decode (enc_mess):
    dec_mess = ""
    for i in range(len(enc_mess)):
        dec_mess += alphabet[int(enc_mess[i], 2)]
    return dec_mess

# otp : Encrypts or decrypts a message using a One-Time Pad (OTP). 
# If the key is not provided, the encryption is done with a random one.
# mess : Message to be encrypted or decrypted.
# key_str : Optional list of 5-bit binary strings to use as the key.
# Returns the encrypted or decrypted message as a string.

def otp (mess, key_str = None):
    enc_mess = encode(mess)
    otp_arr = []
    key = []
    if key_str == None:
        for i in range(len(enc_mess)):
            key.append(format(random.randint(0,31), "05b"))
        print(key)
        for i in range(len(enc_mess)):
            otp_arr.append(format(int(enc_mess[i], 2) ^ int(key[i], 2),"05b"))
        return decode(otp_arr)
    else:
        key = key_str
        for i in range(len(enc_mess)):
            otp_arr.append(format(int(enc_mess[i], 2) ^ int(key[i], 2),"05b"))
        return decode(otp_arr)


# Example of encryption/decryption

mess = "RA/"
key = ['10010', '01010', '11100']
otped = otp(mess,key)
DKA = "DKA"
otped2 = otp(DKA,key)
print(otped)
print(otped2)
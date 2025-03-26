alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.!/()-"

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

# transpose : Transposes the list S = [0, 1, ... , 255] according to seed.
# seed : String seed on which the transposition of array S is depended on.
# Returns the list S transposed.

def transpose(seed):
    S = list(range(256))
    j = 0
    enc_seed = [int(x, 2) for x in encode(seed)]
    for i in range(256):
        j = (j + S[i] + enc_seed[i % len(enc_seed)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

# key_creation : Generates a key. 
# length : Desiered length of the key in number of characters according to alphabet.
# if length = 3, the length of the generated key will be >= 15. 
# S : list by which the generated key is depended.
# Returns the generated key.

def key_creation(length, S):
    i = 0
    j = 0
    K = []
    length = length * 5
    while length > 0:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        byte = format((S[(S[i] + S[j]) % 256]), "08b")
        K.extend(int(b) for b in byte)
        length -= 8
    return K

# RC4 : Encrypts a message.
# mess : Message to be encrypted.
# seed : Seed that will generate the key that encrypts the message.
# Returns the message encrypted.

def RC4(mess, seed):
    cryp_mess = []
    enc_mess = encode(mess)
    S = transpose(seed)
    key = key_creation(len(enc_mess), S)
    for i in range(len(enc_mess)):
        key_bits = "".join(str(b) for b in key[5*i : 5*i+5])
        cryp_mess.append(format(int(enc_mess[i], 2) ^ int(key_bits, 2), "05b")) 
    return decode(cryp_mess)

# Example usage of encryption and decryption

mess = "MISTAKESAREASSERIOUSASTHERESULTSTHEYCAUSE"
seed = "HOUSE"
enc_mess = RC4(mess, seed)

mess2 = "!CIJ(TYRZ(CWTDMOP.ZY!JPRTKBMN!CQAK.B!B/IH"
enc_mess2 = RC4(mess2, seed)

print(enc_mess)
print(enc_mess2)

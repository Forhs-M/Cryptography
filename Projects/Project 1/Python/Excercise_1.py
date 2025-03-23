alphabet = "αβγδεζηθικλμνξοπρστυφχψω"

# decryption : Decrypts the given message
# mess : Greek continuous message ,without spaces between words, to be decrypted
# Returns the decrypted message

def decryption (mess):
    dec_mess = ""
    for char in mess:
        enc_num = alphabet.index(char) + 1
        dec_num = (enc_num - 3) % 24
        if dec_num == 0:
            dec_char = "ω"
        else:
            dec_char = alphabet[dec_num - 1]
        dec_mess += dec_char
    return dec_mess

# Example use of decryption on οκηθμφδζθγοθχυκχσφθμφμχγ

enc_mess = 'οκηθμφδζθγοθχυκχσφθμφμχγ'

mess = decryption(enc_mess)
print(mess)

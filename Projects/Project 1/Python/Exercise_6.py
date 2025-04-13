from collections import deque

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.!/()-"

# the function sumxor
# accepts a binary list of the form [1,0,1,...]
# and returns the xor-sum of the bits

def sumxor(l):
    r = 0
    for v in l: 
        r = r^v
    return r

# the function lfsr accepts three arguments
# seed : a binary list of the form [0,1,1,1,0,1,0,1,...] which is the initial seed
# feedback : a binary list which defined by the feedback polynomail 
# for instance [0,0,1,1]-->x^4+x^3+1
# bits : is an integer, which tells the function to return bits-number of the resulting stream of the lfsr
# the function prints the internal states if flag = 0 and always returns the output

def lfsr(seed,feedback,bits, flag):
    index_of_ones = []
    feedback_new = []
    for i in range(len(feedback)):
        if 1 in feedback:
            index_of_ones.append(feedback.index(1))
            feedback[feedback.index(1)] = 0
    feedback_new = index_of_ones    #this is a list which contains the positions of 1s in feedback list
    seed = deque(seed)              # make a new deque 
    output = []
    if flag==0:
        print('initial seed :',seed)
    for i in range(bits):
        xor = sumxor([seed[j] for j in feedback_new])
        output.append(seed.pop()) #extract to output the right-most bit of current seed
        seed.appendleft(xor)      #insert from left the result of the previous xor 
        if flag==0:
            print('state', i+1, 'of the lfsr :',seed)
    return output

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
    

# key_finder: Finds the key used for OTP encyption on a given pair of a 
# message and its encryption. 
# mess: Message that was encypted.
# enc_mess: Encryption of message.
# Returns the key used for the encryption in 5-bit binary strings.

def key_finder(mess, enc_mess):
    # Κωδικοποίηση του plaintext και του ciphertext
    plaintext_codes = encode(mess)      
    ciphertext_codes = encode(enc_mess)   
    
    key = []
    # XOR για κάθε σύνολο 5-bit
    for i in range(len(plaintext_codes)):
        key_val = int(plaintext_codes[i], 2) ^ int(ciphertext_codes[i], 2)
        key.append(format(key_val, "05b"))
    return key

# seed_finder: Finds the seed used by an LFSR that generates the given key.
# key: 5-bit binary string.
# Returns the seed used to generate the key.

def seed_finder(key):
    """
    Βρίσκει το αρχικό seed (λίστα 10 bits) για έναν LFSR με πολυώνυμο
    x^10 + x^9 + x^7 + x^6 + 1, όπου:
      - Η έξοδος σε κάθε βήμα είναι το bit της θέσης 0 (δηλαδή x^10)
      - Το νέο bit υπολογίζεται ως: 1 XOR state[1] XOR state[3] XOR state[4]
      - Τα πρώτα 10 outputs αγνοούνται και οι επόμενες έξοδοι ομαδοποιούνται σε ομάδες των 5 bits.
      
    Η παράμετρος key αναμένεται να είναι μια λίστα από συμβολοσειρές 5-bit,
    π.χ. ["11111", "00001"].
    
    Επιστρέφει το seed ως λίστα 10 ακεραίων (0 ή 1) ή None εάν δεν βρεθεί.
    """
    # Ο αριθμός των bits που απαιτούνται για το κλειδί
    num_key_bits = 5 * len(key)
    
    # Δοκιμάζουμε όλα τα πιθανά 10-bit seeds (από 0 έως 1023)
    for candidate in range(2**10):
        # Μετατροπή σε λίστα 10 bits, με τη πρώτη θέση να αντιστοιχεί στο x^10.
        seed = [int(b) for b in format(candidate, "010b")]
        state = seed.copy()
        generated_bits = []  # θα συλλέξουμε τα bits που παράγονται μετά τις πρώτες 10 εξόδους
        
        # Ο συνολικός αριθμός επαναλήψεων: 10 (για skip) + όσες θέλουμε για το key
        total_steps = 10 + num_key_bits
        for i in range(total_steps):
            # Έξοδος: το bit από το κουτί x^10 (θέση 0)
            out_bit = state[0]
            # Υπολογισμός του νέου bit: 1 XOR state[1] XOR state[3] XOR state[4]
            new_bit = 1 ^ state[1] ^ state[3] ^ state[4]
            # Shift: αφαιρούμε το πρώτο στοιχείο και προσθέτουμε το νέο στο τέλος.
            state = state[1:] + [new_bit]
            # Αποθηκεύουμε την έξοδο μόνο αφού έχουν περάσει τα πρώτα 10 βήματα (δηλαδή το seed αγνοείται)
            if i >= 10:
                generated_bits.append(str(out_bit))
        
        # Ομαδοποίηση των παραχθέντων bits σε ομάδες των 5 για σύγκριση
        generated_key = [''.join(generated_bits[i*5:(i+1)*5]) for i in range(len(key))]
        
        if generated_key == key:
            return seed  # Επιστρέφουμε το seed αν βρέθηκε ταίριασμα
    
    return None  # Επιστροφή None σε περίπτωση που κανένα seed δεν παράγει το δοθέν key

# Παράδειγμα χρήσης:
# Αν έχουμε το κλειδί της μορφής:
mess = "AB"
enc_mess = "SQ"
key = key_finder(mess, enc_mess)
found_seed = seed_finder(key)

print("Βρέθηκε seed:" if found_seed is not None else "Δεν βρέθηκε seed.", found_seed)

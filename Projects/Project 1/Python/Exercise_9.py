# s : Computes the output of the S-Box S for a given integer in the range [0, 15]  
# inp: An integer in the range [0, 15] representing the 5-bit input 
# Returns the output of the s box

def s(inp):
    output = (inp * inp + 3) % 32 
    return output

# hamming_weight : Calculates the hamming weight of a given integer
# inp : Integer whoose hamming weight will be calculated
# Returns the hamming weight

def hamming_weight(inp):
    return bin(inp).count("1")

# lbn : Computes the Linear Branch Number of the S box S
# Returns the Linear Branch Number of the S box S

def lbn():
    size = 32 
    lbn = float("inf")
    for a in range(1, size):
        for b in range( 1, size):
            count = 0
            for x in range(size):
                ax = bin(a & x).count("1") % 2 
                bSx = bin(b & s(x)).count("1") % 2
                if ax == bSx:
                    count += 1
            if count != size / 2:
                pos_lbn = hamming_weight(a) + hamming_weight(b)
                lbn = min(lbn, pos_lbn)
    return lbn            

# Example of lbn calculation for S Box S

lbn1 = lbn()
print("LBN of S is :", lbn1)

# s5 : Calculates which number should be outputed from S-Box S5
# inp : Input 
# Returns the bitwise exit

def s5(inp):

    row = ((inp >> 5) << 1) | (inp & 1)
    col = (inp >> 1) & 0xF

    s_box = [
        [0b0010, 0b1100, 0b0100, 0b0001, 0b0111, 0b1010, 0b1011, 0b0110,
         0b1000, 0b0101, 0b0011, 0b1111, 0b1101, 0b0000, 0b1110, 0b1001],
        [0b1110, 0b1011, 0b0010, 0b1100, 0b0100, 0b1111, 0b0111, 0b0001,
         0b0101, 0b1000, 0b1101, 0b1010, 0b1001, 0b1001, 0b0000, 0b0110],
        [0b0100, 0b1100, 0b0001, 0b0111, 0b1010, 0b1110, 0b0011, 0b0100,
         0b0111, 0b1000, 0b1111, 0b0000, 0b1101, 0b0010, 0b0000, 0b1110],
        [0b1011, 0b1000, 0b0000, 0b0111, 0b0111, 0b1110, 0b0010, 0b1101,
         0b1111, 0b0000, 0b1011, 0b1010, 0b0100, 0b0101, 0b0101, 0b0011]
    ]
    return s_box[row][col]

# compute_ddt : Computes the differential distribution table s
# Returns the differential distribution table of S-Box s

def compute_ddt():
    ddt = {}
    for i in range(64):
        ddt[i] = {j: 0 for j in range(16)}
        for x in range(64):
            xp = x ^ i
            j = s5(x) ^ s5(xp)
            ddt[i][j] += 1
    return ddt

# differential_uniformity : Computes the differential uniformity of a differential distribution table
# ddt : The differential distribution table 
# Returns the differential uniformity

def differential_uniformity(ddt):
    dif_uni = 0
    for i in range(1, 64):
        for j in range(16):
            if ddt[i][j] > dif_uni:
                dif_uni = ddt[i][j]
    return dif_uni


ddt = compute_ddt()
du = differential_uniformity(ddt)
print("Diff(S_5) = ", du)
   

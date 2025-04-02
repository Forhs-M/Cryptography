# s: Computes the output of the S-Box S for a given 6-bit input.
#     The row is determined by combining the first and last bit of the input (bit 5 and bit 0).
#     The column is determined by the middle 4 bits (bits 1 to 4).
# inp: An integer in the range [0, 63] representing the 6-bit input.
# Returns: The integer output value from the S-Box.

def s(inp):
    row = ((inp >> 5) << 1) | (inp & 1)
    col = (inp >> 1) & 0xF

    s_box = [
        [0, 2, 3, 7, 9, 12, 15, 7, 6, 15, 15, 1, 7, 3, 1, 0],
        [1, 5, 6, 13, 4, 1, 5, 11, 7, 8, 7, 1, 1, 3, 2, 13],
        [5, 3, 5, 12, 11, 1, 1, 5, 13, 0, 15, 7, 2, 2, 13, 0],
        [3, 12, 3, 11, 2, 2, 2, 4, 6, 5, 5, 0, 4, 3, 1, 0]
    ]
    return s_box[row][col]

# compute_ddt : Computes the differential distribution table S
# Returns the differential distribution table of S-Box S

def compute_ddt():
    ddt = {}
    for i in range(64):
        ddt[i] = {j: 0 for j in range(16)}
        for x in range(64):
            xp = x ^ i
            j = s(x) ^ s(xp)
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

# Example of computing the ddt of S and printing its differential uniformity

ddt = compute_ddt()
du = differential_uniformity(ddt)
print("Diff(S) = ", du)

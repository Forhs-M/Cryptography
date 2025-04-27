import math

def karatsuba(a,b):
    if(a <100 or b<100):
        return a*b
    m1 = max(math.log(a,10),math.log(b,10))
    m2 = math.floor(m/2)


# fastmod: given base, exp and m calculates (base^exp)%m faster than the calculation of it.
# base: int
# exp: int
# m: int
# Returns (base^exp)%m 

def fastmod(base, exp, m):
    result = 1
    while (exp > 0):
        if(exp%2 == 1):
            result = (result * base) % m
        exp = exp/2
        base = base^2 % m
    return result

res = fastmod(2, 53, 157)
print(res)
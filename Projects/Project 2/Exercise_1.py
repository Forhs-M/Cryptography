import math

# karatsuba: given a and b calculates the product a*b faster
# a: integer
# b: integer
# Returns a*b
def karatsuba(a,b):
    if(a <100 or b<100):
        return a*b
    m1 = max(math.log(a,10),math.log(b,10))
    m2 = math.floor(m1/2)
    high_a = a // 10**m2
    low_a = a % 10**m2
    high_b = b // 10**m2
    low_b = b % 10**m2
    z0 = karatsuba(low_a, low_b)
    z1 = karatsuba((low_a + high_a), (low_b + high_b))
    z2 = karatsuba(high_a, high_b)
    result = z2 * 10**(2 * m2) + (z1 - z2 - z0) * 10**m2 + z0
    return result

# fastmod: given base, exp and m calculates (base^exp)%m faster than the calculation of it.
# base: integer
# exp: integer
# m: integer
# Returns (base^exp)%m 

def fastmod(base, exp, m):
    result = 1
    while (exp > 0):
        if(exp%2 == 1):
            result = (result * base) % m
        exp = exp//2
        base = base**2 % m
    return result

# Example

res1 = fastmod(2,1000,2**107-1)
res2 = fastmod(3,101,2**107-1)
res3 = fastmod(5,47,2**107-1)
prod_1 = karatsuba(res1,res2)
result = karatsuba(prod_1,res3)
print(res1)
print(res2)
print(res3)
print(result)
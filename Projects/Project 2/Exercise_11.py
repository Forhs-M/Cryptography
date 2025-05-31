import math
import random

# is_prime : CHecks if an integer is prime
# num : Integer
# Returns true if num is prime else false

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# poly : Calcutes y = f(x) 
# f : List containing coefficients of the polynomial
# x : Integer
# Returns the calculated value 

# Example: poly([0,2,1],2)
# sum = 0*2^0 + 2*2^1 + 1*2^2 = 8

def poly(f,a):
    sum = 0
    for i in range(len(f)):
        sum += f[i]*a**i
    return sum  

# modifiedFLoyd : Searches for a non trivial divisor of a given Integer 
# f : List containing coefficients of the polynomial
# N : Integer
# Returns a non trivial divisor of N if it is not prime else returns 0 

def modifiedFloyd(f,N):
    if is_prime(N):
        return 0
    
    iters = 0
    x = random.randint(2,N-1)
    y = x
    while(1):
        iters += 1
        x = poly(f,x)
        y = poly(f,poly(f,y))
        a = math.gcd(abs(x-y),N)
        if 1<a<N: 
            return a
        if (iters > 10**5):
            iters = 0
            x = random.randint(2,N-1)

print(modifiedFloyd([1,1], 2**800-1))

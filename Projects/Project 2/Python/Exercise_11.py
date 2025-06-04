import math
import random

# poly : Calcutes y = f(x). 
# f : List containing coefficients of the polynomial.
# x : Integer.
# N : mod.
# Returns the calculated value. 

# Example: poly([0,2,1],2)
# sum = 0*2^0 + 2*2^1 + 1*2^2 = 8

def poly(f, a, N):
    sum = 0
    for i in range(len(f)):
        sum = (sum + f[i] * pow(a, i, N)) % N
    return sum

# modifiedFLoyd : Searches for a non trivial divisor of a given integer. 
# f : List containing coefficients of the polynomial.
# N : Integer.
# Returns a non trivial divisor of N if it is not prime else returns 0. 

def modifiedFloyd(f,N):

    x = random.randint(2,N-1)
    y = x
    while(1):   
        x = poly(f,x,N)
        y = poly(f,poly(f,y,N),N)
        a = math.gcd(abs(x-y)%N,N)
        if 1<a<N: 
            return a
        if a == N:   
            x = random.randint(2,N-1)
            y = x

print(modifiedFloyd([1,0,1], 2**257 -1 ))

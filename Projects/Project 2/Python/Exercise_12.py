import math

# factor: Given a number n, calculates if it a product of 2 prime numbers
# n: Number
# Returns the 2 primes whose product is n

def factor(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return i , n // i
    return None, None

# phi : Given a number n which is a prouct of 2 primes calculates φ(n)
# n : Number
# Returns φ(n)

def phi(n):
    p,q = factor(n)
    return (p-1)*(q-1)

# inverse: Given e and N (public key) calculates d (private key)
# e : Part of public key
# N : Part of public key
# Returns inverse of e, d (private key)

def inverse(e,N):
    phi_of_n = phi(N)    
    x = 0
    new_x = 1
    y = phi_of_n 
    new_y = e
    while(new_y != 0):
        quot = y // new_y
        temp = x
        x = new_x
        new_x = temp - quot*new_x
        temp = y
        y = new_y
        new_y = temp - quot*new_y
    if x < 0:
        x = x + phi_of_n
    return x

# decrypt : Decrypts a message encoded by RSA
# c : Message to be decrypted.  
# N : part of public key
# e : part of public key
# Returns the decrypted message

def decrypt(c,e,N):
    d = inverse(e,N)
    decoded = ''
    for i in c:
        m = i ** d % N
        decoded += chr(m)
    return decoded

# Example of decryption

c = [3203, 909, 3143, 5255, 5343, 3203, 909, 9958, 5278, 5343, 9958, 5278,
     4674, 909, 9958, 792, 909, 4132, 3143, 3203, 5343, 792, 3143, 4443]

print(decrypt(c,19,11413)) 
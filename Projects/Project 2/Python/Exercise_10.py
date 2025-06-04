import math
import random

# extended_gcd : Extended Euclidean Algorithm.
# a : Integer.
# b : Integer.
# Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).

def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)

# mod_inverse : Computes modular inverse of a modulo m.
# a : Integer.
# m : Integer (modulus).
# Returns x such that (a*x) mod m = 1  if it exists else 0. 

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return 0
    return x % m


# pollard_dlog : Pollard’s Rho for discrete logarithm. 
# g : Integer.
# h : Integer. 
# p : prime for mod. 
# Returns x such that (g^x) mod p = h.

def pollard_d_log(g, h, p):
    N = p - 1
    while True:
        a0 = random.randint(0, N - 1)
        b0 = random.randint(0, N - 1)
        x0 = (pow(g, a0, p) * pow(h, b0, p)) % p

        # f : Pseudorandom function that updates x, a, b based on x.
        # state = (x_val, a_val, b_val).
        # Returns a new set (x_new, a_new, b_new).
        def f(state):
            x_val, a_val, b_val = state
            if x_val % 3 == 0:
                return ((x_val * g) % p, (a_val + 1) % N, b_val)
            elif x_val % 3 == 1:
                return ((x_val * x_val) % p, (2 * a_val) % N, (2 * b_val) % N)
            else:
                return ((x_val * h) % p, a_val, (b_val + 1) % N)
        slow = f((x0, a0, b0))
        fast = f(f((x0, a0, b0)))
        while slow[0] != fast[0]:
            slow = f(slow)
            fast = f(f(fast))
        _, a1, b1 = slow
        _, a2, b2 = fast
        numer = (a2 - a1) % N
        denom = (b1 - b2) % N
        inv_denominator = mod_inverse(denom, N)
        if inv_denominator == 0:
            continue
        x = (numer * inv_denominator) % N
        return x

# Example of usage

print(pollard_d_log(2, 2763, 3571))
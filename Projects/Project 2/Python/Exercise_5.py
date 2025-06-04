import math

# sieve : Implemets the sieve algorithm until a given integer
# N : Given integer
# Returns a list of N elements where sigma[i] = addition of i's divisors

def sieve(N):
    sigma = [0]*N
    for i in range(1,N):
        for j in range(i, N, i):
            sigma[j] +=i
    return sigma

# ineq_check : checks if the given inequality is true every odd integer < given integer
# N : Given integer
# Returns true if the inequality is true else returns false and prints the number which does not satisfy the inequality 

def ineq_chek(N):
    e_g = math.exp(0.5772)
    sigma = sieve(N)
    for i in range (3, N, 2):
        left = sigma[i] / i
        lnln = math.log(math.log(i))
        right = (e_g/2) * lnln + 0.74/lnln
        if right < left:
            print(i,"does not satisfy the inequation")
            return False
    return True

# Example of usage 

print(ineq_chek(2**20))
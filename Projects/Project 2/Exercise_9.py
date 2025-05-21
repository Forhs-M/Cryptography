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

# trial_division : Given an integer calculates its prime factors 
# num : Integer
# REturns a list containing : Returns a list containing every prime factor of num

def trial_division(n):
    primelist = []
    i = 2
    while i <= n:
        if is_prime(i) and n % i == 0:
            primelist.append(i)
            n //= i  
        else:
            i += 1
    return primelist    

# Example

test = trial_division(2**62-1)
print("Prime array", test)  
# trial_division : Given an integer calculates its prime factors. 
# num : Integer.
# Returns a list containing every prime factor of num.

def trial_division(n):
    primelist = []
    i = 3
    while i*i <= n:
        if  n % i == 0:
            primelist.append(i)
            n //= i  
        else:
            i += 2
    if n > 1:
        primelist.append(n)
    return primelist    

# Example of usage.

test = trial_division(2**62-1)
print("Prime array", test)  
# fastmod: given base, exp and m calculates (base^exp)%m faster than the calculation of it.
# base: Integer.
# exp: Integer.
# m: Integer.
# Returns (base^exp)%m. 

def fastmod(base, exp, m):
    result = 1
    while (exp > 0):
        if(exp%2 == 1):
            result = (result * base) % m
        exp = exp//2
        base = base**2 % m
    return result

# fermat_test : Performs Fermat's test on a given number for every given base. 
# N : Given number. 
# bases: Given bases.
# Returns True if number passed Fermat's test for every given base else False.

def fermat_test(N,base):
    for b in base:
        a = fastmod(b, N-1, N)
        if a != 1:
            print("Given number failed Fermat's test for ", b, "base")
            return False
    print(" Given number passed Fermat's test for given bases.")
    return True    
    
# Example of usage.

fermat_test(3714089895285 * (2**60000) - 1, [2,3,5,7])
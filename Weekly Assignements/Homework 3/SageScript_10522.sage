import random

x = PolynomialRing(GF(2), 'x').gen()

# Input the degree of the polynomial 
n = 4

d = []
# Find every divisor of 2^n - 1 that is not 1, 2^n - 1
for i in range (2, 2^n - 1):
    if (2^n - 1) % i == 0:
        d = d + [i]
        
g = x^(2^n - 1) - 1 


check = 0
while check == 0:
    max = 1
    coef = [1]
    # Create n-2 random coefficients of the polynomial
    for i in range (n-1):
        rand_coef = random.randint(0, 1)
        coef = coef + [rand_coef]
        
    coef = coef + [1] # Make the polynomial n-th grade   
    f = sum(coef[i] * x^i for i in range(len(coef)))
    
    if f.is_irreducible(): # If the polynomial is irreducible continue, else repeat the proccess
        if g % f == 0: 
            for i in d:
                if (x^((2^n - 1)/i) - 1) % f == 0:
                    max = 0 
                    break
             
            if max == 1:
                check = 1
            
print(f)            
       
 

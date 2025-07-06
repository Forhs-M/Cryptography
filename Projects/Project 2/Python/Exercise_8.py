# is_prime : Checks if an integer is prime.
# num : Integer.
# Returns true if num is prime else false.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# fastmod: For given base, exp and m calculates (base^exp)%m faster than the calculation of it.
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

# find_s_t : For a given odd number calculates s and t where num - 1 = (2^s)*t.
# num : Given odd number.
# Returns s and t.

def find_s_t(num):
    t = num -1
    s = 0
    while t % 2 == 0:
        t = t //2
        s += 1
    return s, t

# find_strong_pseudo : For a given base find the smallest strong sudo prime for this base.
# base : Given base.
# Returns the smallest strong sudo prime of given base.

def find_strong_pseudo(base):
    num = 3
    while True:
        if is_prime(num):
            num += 2
            continue
        s, t = find_s_t(num)
        b = fastmod(base, t, num)
        if b == 1 or b == num -1:
            return num
        else:
            for  i in range(s-1):
                if(b ** (2**i)) % num == num-1:
                    return num
        num += 2

# Example of usage

x = find_strong_pseudo(32)
print(x)
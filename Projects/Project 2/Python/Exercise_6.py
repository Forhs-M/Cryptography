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

def next_perfect_number(after):
    p = 2
    while True:
        mersenne = 2 ** p - 1
        if is_prime(mersenne):
            perfect = 2 ** (p - 1) * mersenne
            if perfect > after:
                return perfect
        p += 1

# Example: Find the next perfect number after 8128.

print(next_perfect_number(8128))

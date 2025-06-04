import math

# cont_frac: Calculates the contiued fraaction e/N.
# e : Numerator.
# N : Denumerator.
# Returns a list that is the continued fraction e/N.

def cont_frac(e,N):
    cont = []
    while N>0:
        fact = e // N
        cont.append(fact)
        temp = N
        N = e - fact*N
        e = temp
    return cont 

# conv : Given a continued fraction, calculates its convergents.
# cont : List that represents a continued fraction.
# Returns a list containing pairs of k,d (k/d).

def conv(cont):
    conv_list = []
    k1 = 1
    k2 = 0
    d1 = 0
    d2 = 1 
    for q in cont:
        k = q*k1 + k2
        d = q*d1 + d2
        conv_list.append((k,d))
        k2 = k1
        k1 = k
        d2 = d1
        d1 = d
    return conv_list

# is_perf_sq : Given a number, finds if it is a perfect square.
# num : Given number.
# Returns True if num is a perfect square else False.

def is_perf_sq(num):
    root = int(math.isqrt(num))
    return root**2 == num

# try_conv : Given a convergant decides if it can produce possible φ(Ν).
# k : Numerator of convergant.
# d : Denumerator of convergant.
# e : Part of public key.
# N : Part of public key.
# Returns 0 if φ(N) is not possible else d.

def try_conv(k,d,e,N):
    if k == 0:
        return k
    poss_phi = (e*d-1) // k
    if  (e*d-1) % k != 0:
            return 0
    disc = (-(N - poss_phi +1))**2 - 4*N
    if disc >= 0 and is_perf_sq(disc):
        root = int(math.isqrt(disc))
        x1 = (-(N - poss_phi +1) + root) // 2 
        x2 = (-(N - poss_phi +1) - root) // 2 
        if x1 * x2 == N:
            return  d
    return 0

# Wiener : given a public key, performs Wiener attack in order to find the private key.
# e : Part of public key.
# N : Part of public key.
# Returns the private key d if found else None.

def Wiener(e,N):
    cont = cont_frac(e,N)
    conv_list = conv(cont)
    for k,d in conv_list:
        if d == 0:
            continue
        if(try_conv(k,d,e,N)):
            return d
    return None


# decrypt : Decrypts a message encoded by RSA.
# c : Message to be decrypted.  
# N : part of public key.
# e : part of public key.
# Returns the decrypted message if found else an error message.

def decrypt(c,e,N):
    d = Wiener(e,N)
    if d == 0:
        mess = "Something went wrong, private key not found"
        return mess
    decoded = ''
    for i in c:
        m = i ** d % N
        decoded += chr(m)
    return decoded

# Example of decription. 

c=[47406263192693509,51065178201172223,30260565235128704,82385963334404268,
8169156663927929,47406263192693509,178275977336696442,134434295894803806,
112111571835512307,119391151761050882,30260565235128704,82385963334404268,
134434295894803806,47406263192693509,45815320972560202,174632229312041248,
30260565235128704,47406263192693509,119391151761050882,57208077766585306,
134434295894803806,47406263192693509,119391151761050882,47406263192693509,
112111571835512307,52882851026072507,119391151761050882,57208077766585306,
119391151761050882,112111571835512307,8169156663927929,134434295894803806,
57208077766585306,47406263192693509,185582105275050932,174632229312041248,
134434295894803806,82385963334404268,172565386393443624,106356501893546401,
8169156663927929,47406263192693509,10361059720610816,134434295894803806,
119391151761050882,172565386393443624,47406263192693509,8169156663927929,
52882851026072507,119391151761050882,8169156663927929,47406263192693509,
45815320972560202,174632229312041248,30260565235128704,47406263192693509,
52882851026072507,119391151761050882,111523408212481879,134434295894803806,
47406263192693509,112111571835512307,52882851026072507,119391151761050882,
57208077766585306,119391151761050882,112111571835512307,8169156663927929,
134434295894803806,57208077766585306]

print(decrypt(c,50736902528669041,194749497518847283))
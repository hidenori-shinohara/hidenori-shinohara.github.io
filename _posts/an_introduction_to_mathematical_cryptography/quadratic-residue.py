
def slow_inverse(k, m):
    for i in range(m):
        if (k * i) % m == 1:
            return i
    print("unable to find inverse")
    return 0
def slow_pow(p, e):
    r = 1
    for i in range(e):
        r = r * p
    return r
    

p = 7
b = 2

# Solve x^2 = b (mod p)

alpha = 0
for x in range(p):
    if (x * x) % p == b:
        print("found a solution {} * {} = {} (mod {})".format(x, x, b, p))
        alpha = x
        break

beta = alpha
for e in range(1, 10):
    pe = slow_pow(p, e)
    peplus1 = slow_pow(p, e + 1)
    m = (beta * beta) // pe
    l = (-m * slow_inverse(2, p) * slow_inverse(beta, p)) % p
    gamma = (l * slow_pow(p, e) + beta) % peplus1
    # Print all variables
    print("p = {}".format(p))
    print("b = {}".format(b))
    print("e = {}".format(e))
    print("pe = {}".format(pe))
    print("peplus1 = {}".format(peplus1))
    print("m = {}".format(m))
    print("l = {}".format(l))
    print("gamma = {}".format(gamma))
    if (gamma * gamma - b) % peplus1 == 0:
        print("{} * {} == {} (mod {})".format(gamma, gamma, b, peplus1))
    else:
        print("{} * {} != {} (mod {})".format(gamma, gamma, b, peplus1))
    beta = gamma
    print()
    print()
    print()










    

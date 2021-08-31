
def isprime(a):
    if a == 1:
        return 0
    i = 2
    while i * i <= a:
        if a % i == 0:
            return 0
        i += 1
    return 1


def primes_list(a, b):
    p = 0
    for i in range(a, b):
        if isprime(i):
            p += 1
            print(i, end=' ')
            if p % 20 == 0:
                print()
    print()


primes_list(990000, 1000000)

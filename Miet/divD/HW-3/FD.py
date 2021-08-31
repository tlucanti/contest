def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def nums_bezu(a, b):
    x1, x2, y1, y2 = 0, 1, 1, 0
    while b > 0:
        q = a // b
        r = a - q*b
        x = x2 - q*x1
        y = y2 - q*y1
        a, b, = b, r
        x2, x1 = x1, x
        y2, y1 = y1, y
    return x2, y2


def diophant(c, a, b):
    if c == 0:
        return 0, 0
    d = gcd(a, b)
    if d == 0 or c % d != 0:
        return None
    else:
        u, v = nums_bezu(a // d, b // d)
        u, v = -u * c // d, -v * c // d
        if abs(u) > 1000000000000 or abs(v) > 1000000000000:
            return None
        return u, v


def solve(a, p):
    if p == 1:
        return -1
    b = diophant(1, a, p)
    if b is None:
        return -1
    else:
        b, k = b[0], b[1]
        if b < 0:
            return -b
        else:
            return -b + p // gcd(a, p)


for q in range(int(input())):
    a, p = input().split()
    a, p = int(a), int(p)
    print(solve(a, p))


# from random import randint as rand
# maxx = 100
# for q in range(100000):
#     # if q % 100 == 0:
#         # print()
#         # pass
#     a = rand(0, maxx - 1)
#     # a = 0
#     # p = rand(a + 1, maxx)
#     p = 1
#     b = solve(a, p)
#     if b == -1:
#         # print('.', end='')
#         continue
#     # print('|', end='')
#     if b > p or b < 1:
#         print("Border error", a, b, p)
#     if (a * b) % p != 1:
#         print("Answer error", a, b, p)

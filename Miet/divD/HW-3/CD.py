
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


def solve(c, a, b):
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


__input__ = open('input.txt', 'r')
# __output__ = open('outputpy.txt', 'w')
input = __input__.readline
# print = lambda *args, sep=' ', end='\n': __output__.write(sep.join(map(str, args)) + end)


for t in range(int(input())):
    c, a, b = input().split()
    a, b, c = int(a), int(b), int(c)
    s = solve(c, a, b)

    if s is None:
        if a != b:
            print('\nNone', c, a, b, end='')
        pass
    elif c + a * s[0] + b * s[1] != 0:
        print('\nWrong', c, a, b, '->', s[0], s[1], end='')
        pass
    elif abs(s[0]) > 1e11 or abs(s[1]) > 1e11:
        print('\nBig', c, a, b, '->', s[0], s[1], end='')
        pass

    # if s is None:
    #     print('No solution')
    # else:
    #     print(*s)


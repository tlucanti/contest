
import math as m

def inp():
    return list(map(int, input().split()))

def _g(_a, _b):
    return m.floor(m.sqrt(_a * _b))

def __g(_a, _b):
    return m.isqrt(_a * _b)

def ___g(_a, _b):
    y = _a * _b
    L = 0;
    R = y + 1;

    while( L != R - 1 ):
        M = (L + R) / 2;
        if( M * M <= y ):
            L = M;
        else:
            R = M;
    return L;

def isq(n):
    _s = m.floor(m.sqrt(n)) - 2
    while _s * _s <= n:
        _s += 1
    return _s

def g(_a, _b):
    return isq(_a * _b)

def solve_wrong(x, y, z):
    r1, r2 = -20, 21

    a = x * y // z
    b = x * z // y
    c = y * z // x

    for da in range(r1, r2):
        if a + da <= 0:
            continue
        for db in range(r1, r2):
            if b + db <= 0:
                continue
            for dc in range(r1, r2):
                if c + dc <= 0:
                    continue
                aa = a + da
                bb = b + db
                cc = c + dc
                if x == g(aa, bb) and y == g(aa, cc) and z == g(bb, cc):
                    return aa, bb, cc
    return 0, 0, 0

def solve_slow(x, y, z):
    x, y, z = sorted([x, y, z])
    m = 2 * max(x, y, z) + 1
    a = x * y // z
    b = x * z // y
    c = y * z // x
    print((a,b,c))
    print(g(a,b),g(a,c),)
    for a in range(m):
        for b in range(a, m):
            for c in range(b, m):
                if x == g(a, b) and y == g(a, c) and z == g(b, c):
                    print(a, b, c)

for _ in range(int(input())):
    print(*solve_wrong(*inp()))


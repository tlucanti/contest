
def inp():
    return list(map(int, input().split()))

def slow(a, b, c):
    s = set()
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                s.add(i + 2 * j + 3 * k)
    return len(s) - 1

def solve(a, b, c):
    A = a
    if a >= 2:
        A = 2
    B = b
    if b >= 2:
        B = 2

    q = (A, B)
    ans = 0
    if q == (0, 0):
        ans = c
    elif q == (1, 0):
        ans = 1 + 2 * c
    elif q == (2, 0):
        ans = 3 * c + a
    elif q == (0, 1):
        ans = 1 + 2 * c
    elif q == (1, 1):
        ans = 3 * c + 2 * b + a
    elif q == (2, 1):
        ans = 3 * c + 2 * b + a
    elif q == (0, 2):
        if c == 0:
            ans = b
        elif c == 1:
            ans = 1 + 2 * b
        else:
            ans = 3 * c + b
    elif q == (1, 2):
        ans = 3 * c + 2 * b + a
    elif q == (2, 2):
        ans = 3 * c + 2 * b + a
    return ans

for i in range(11):
    for j in range(11):
        for k in range(11):
            s1 = solve(i, j, k)
            s2 = slow(i, j, k)
            if s1 != s2:
                print((i, j, k), 'expected:', s2, 'got:', s1)


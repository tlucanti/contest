import sys

def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    l = 0
    r = n - 1
    s = [0] * n
    s[0] = a[0]
    for i in range(1, n):
        s[i] = s[i - 1] + a[i]

    while r - l > 1:
        c = (r + l) // 2
        expected = 0
        print('?', c - l, end=' ')
        for i in range(l, l + c):
            print(i + 1, end=' ')
            expected += a[i]
        print()
        sys.stdout.flush()
        sm = int(input())
        if sm == expected:
            l = c
        else:
            r = c
    print('?', 1, l + 1)
    sys.stdout.flush()
    sm = int(input())
    if sm == 2:
        print('!', l + 1)
    else:
        print('!', r + 1)
    sys.stdout.flush()

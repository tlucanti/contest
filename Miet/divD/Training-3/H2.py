import math


def issqr(a):
    if a < 0:
        return 0
    i = int(math.sqrt(a)) - 1
    while i * i <= a:
        if i * i == a:
            return i
        i += 1
    return 0


n = int(input())
f = True
for i in range(1, n * n):
    b = issqr(n * n - i * i)
    if b != 0:
        print(i, b)
        f = False
        break
    b = issqr(n * n + i * i)
    if b != 0:
        print(i, b)
        f = False
        break
if f:
    print(-1)

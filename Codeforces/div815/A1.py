
import math
from collections import Counter as multiset
from functools import reduce


def inp():
    return list(map(int, input().split()))


def factor(n):
    i = 2
    a = multiset()
    while i * i <= n:
        if n % i == 0:
            a[i] = a.get(a[i], 0) + 1
            n //= i
        else:
            i += 1
    if n > 0:
        a[n] = a.get(a[n], 0) + 1
    return a


for _ in range(int(input())):
    a, b, c, d = inp()
    if a == 0 and c == 0:
        print(0)
        continue
    if a == 0 or c == 0:
        print(1)
        continue

    if a == c and b == d:
        print(0)
        continue
    if a == c or c == d:
        print(1)

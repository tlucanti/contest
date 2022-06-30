
from collections import Counter as multiset


def inp():
    return list(map(int, input().split()))


def factor(n):
    ans = multiset()
    i = 2
    while i * i <= n:
        if n % i == 0:
            ans[i] += 1
            n //= i
        else:
            i += 1
    if n != 1:
        ans[n] += 1
    return ans


for _ in range(int(input())):
    a, b = inp()
    a, b = factor(a), factor(b)
    gcd = a & b
    a -= gcd
    b -= gcd
    maxa = max(a) if len(a) > 0 else 1
    maxb = max(b) if len(b) > 0 else 1
    gcd[max(maxa, maxb)] += 1
    ans = 1
    for i in gcd:
        ans *= i ** gcd[i]
    print(ans)

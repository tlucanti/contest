import math as m
import itertools

def inp():
    return list(map(int, input().split()))

def check_set(pp):
    ans = True
    for i in range(len(pp[0])):
        a = pp[0][i] == pp[1][i] == pp[2][i]
        a |= pp[0][i] + pp[1][i] + pp[2][i] == 6
        ans += a
    return ans == len(pp[0])

def check_meta(p):
    A = 0
    for pp in itertools.combinations(p, 3):
        A += check_set(pp)
    return A > 1

for _ in range(1):
    n, k = inp()
    a = [inp() for i in range(n)]
    ans = 0
    for p in itertools.combinations(a, 5):
        ans += check_meta(p)
    print(ans)

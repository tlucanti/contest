
import math as m

P = 998244353

def solve(n):
    if n > 2:
        prev = solve(n - 2)
        w = m.comb(n - 1, n // 2) + prev[1]
        l = m.comb(n, n // 2) - w - 1
        return w, l
    else:
        return 1, 0

for _ in range(int(input())):
    n = int(input())
    s = solve(n)
    print(s[0] % P, s[1] % P, 1)

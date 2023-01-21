
import math

MOD = 1000000007

def sm(a):
    return (a * (a + 1)) // 2

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
    else:
        s = sm(n - 1) * 2
        f = 1
        for i in range(2, n + 1):
            f = (f * i) % MOD
        # print(s, f)
        print((s * f) % MOD)

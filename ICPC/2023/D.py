
from collections import defaultdict

def euler(x):
    div = defaultdict(int)

    i = 2
    while x > 1 and i * i <= x:
        if x % i == 0:
            div[i] += 1
            x //= i
        else:
            i += 1
    if x > 1:
        div[x] += 1

    ans = 1
    for d in div:
        ans *= div[d] + 1

    return ans

r, q = int(input()), int(input())

ans = euler(r * q - r)
print(ans)

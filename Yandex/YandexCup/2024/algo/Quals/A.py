
import math

def log(*args):
    pass

#log = print

def lcm(a, b):
    return a * b // math.gcd(a, b)

def nr_div(n, a, b, c):
    ab = lcm(a, b)
    ac = lcm(a, c)
    bc = lcm(b, c)
    abc = lcm(lcm(a, b), c)

    return n // ab + n // ac + n // bc - 3 * (n // abc)

def solve(n, a, b, c):
    low = 1
    high = n * lcm(lcm(a, b), c)
    log('high', high)

    while high - low > 1:
        mid = (low + high) // 2
        nr = nr_div(mid, a, b, c)
        if nr == n:
            log('ok', mid)
            high = mid
            break
        elif nr < n:
            log('low', nr)
            low = mid
        else:
            log('high', nr)
            high = mid

    while nr_div(high, a, b, c) == n:
        log('check', mid)
        high -= 1
    return high + 1

a, b, c = [int(x) for x in input().split()]
n = int(input())

if a == b or b == c:
    print(-1)
else:
    ans = solve(n, a, b, c)
    if ans > 1000000000000000000:
        print(-1)
    else:
        print(ans)


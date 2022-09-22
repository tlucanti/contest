
import math as m

def inp():
    return list(map(int, input().split()))

def diofant(n, x, y):
    gcd = m.gcd(x, y)
    if n % gcd != 0:
        return None



for _ in range(int(input())):
    n, x, y = inp()


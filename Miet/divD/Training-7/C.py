
from math import sqrt

def check(x, y, r):
    if (sqrt(x*x + y*y) - r >= R - d) and (sqrt(x*x + y*y) + r <= R):
        return True
    else:
        return False


R, d = map(int, input().split())
n = int(input())
ans = 0
for i in range(n):
    x, y, r = map(int, input().split())
    ans += check(x, y, r)
print(ans)

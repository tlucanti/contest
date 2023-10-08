
import math

k = int(input())
a = [int(input()) for _ in range(k)]

left = 360
for i in a:
    left -= 180 - i

if left < 0:
    print(-1)
elif left == 0:
    print(k, k)
else:
    if k == 1:
        print(3, left + k)
    else:
        if left >= 180:
            mn = max(4, k + 2)
        else:
            mn = max(3, k + 1)
        print(mn, left + k)



from collections import defaultdict

last = defaultdict(int)

n = int(input())
a = [int(_) for _ in input().split()]

for i in range(len(a)):
    last[a[i]] = i

ans = 0
prev = -1
for i in range(1, n + 1):
    if i in last:
        if last[i] > prev:
            ans += 1
            prev = last[i]
            continue
    break
print(ans)


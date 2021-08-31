
n = int(input())
a = list(map(int, input().split()))
d = a[1] - a[0]
f = 1
for i in range(2, n):
    if a[i] - a[i - 1] != d:
        f = 0
        break
if f:
    print(a[-1] + d)
else:
    print(a[-1])

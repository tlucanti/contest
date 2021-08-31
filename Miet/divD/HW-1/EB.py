
n = int(input())
d1 = [0 for i1 in range(1999)]
d2 = [0 for i2 in range(1999)]
s = 0
for i in range(n):
    x, y = input().split()
    x, y = int(x) - 1, int(y) - 1
    d1[x - y] += 1
    d2[1000 - x - y] += 1
for j in range(1999):
    s += d1[j] * (d1[j] - 1) // 2
    s += d2[j] * (d2[j] - 1) // 2
print(s)

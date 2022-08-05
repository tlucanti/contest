
def inp():
    return list(map(int, input().split()))


n, k = inp()
a = [0] * (n + 1)
a[0] = 1
for i in range(1, n):
    for j in range(i, -1, -k):
        a[i] += a[j]
    k += 1
print(*a)
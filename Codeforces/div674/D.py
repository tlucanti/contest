
def check_a(arr, b, c):
    z = 0
    if c - b == 1:
        return 1
    for j in range(b + 1, c):
        s += a[j]
        if s == 0:
            z += check_a(arr, i, j)


n = int(input())
a = list(map(int, input().split()))
z = 0
i = 0
while i < n - 1:
    s = a[i]
    for j in range(i + 1, n):
        s += a[j]
        if s == 0:
            z += 1
            # i = j - 1
            break
    i += 1
print(z)

n = int(input())
a = [int(input()) for _ in range(n)]

a[0] = max(0, a[0] - 1)
for i in range(1, n):
    a[i] = max(a[i - 1] + 1, a[i] - i - 1)

print(*a, sep='\n')


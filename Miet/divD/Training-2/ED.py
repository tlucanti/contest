
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
b.sort()
i = 0
j = 0
while i < n and j < m:
    while a[i] == b[j]:
        j += 1
        
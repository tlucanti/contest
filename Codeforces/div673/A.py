
t = int(input())
for i in range(t):
    n, k = input().split()
    n, k = int(n), int(k)

    a = list(map(int, input().split()))
    m = a[0]
    mi = 0
    for i in range(n):
        if a[i] < m:
            mi = i
            m = a[i]
    s = 0
    for i in range(n):
        if i == mi:
            continue
        s += (k - a[i]) // m
    print(s)

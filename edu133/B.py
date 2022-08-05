
for _ in range(int(input())):
    n = int(input())
    a = list(range(1, n + 1))
    print(n)
    print(*a)
    for i in range(n - 1):
        a[i], a[i + 1] = a[i + 1], a[i]
        print(*a)

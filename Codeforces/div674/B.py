
t = int(input())
for i in range(t):
    n, m = input().split()
    n, m = int(n), int(m)
    f = False
    for i in range(n):
        a, b = input().split()
        c, d = input().split()
        a, b, c, d = [int(i) for i in (a, b, c, d)]
        if b == c:
            f = True
    if f and m % 2 == 0:
        print("Yes")
    else:
        print("No")

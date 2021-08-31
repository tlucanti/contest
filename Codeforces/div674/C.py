
t = int(input())
for i in range(t):
    s = 1
    x = 0
    l = 1
    n = int(input())
    while x * x < n:
        x += 1
    if x == 1:
        print(0)
    else:
        print((n - 1) // x + x - 1)

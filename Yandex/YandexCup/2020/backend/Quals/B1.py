
n, x, k = input().split()
n, x, k = int(n), int(x), int(k)

a = list(map(int, input().split()))

t = 1
b = 0
while 1:
    t
    for i in a:
        if ((t - i) % x) == 0 and t >= i:
            b += 1
            break
    if b == k:
        print(t)
        break
    t += 1

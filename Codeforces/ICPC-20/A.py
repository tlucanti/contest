
t = int(input())
i = 0
while i < t:
    s = 0
    n = int(input())
    while n >= 1:
        if n % 2 == 0:
            n = n // 2
            s += n
        else:
            s += 1
            n -= 1
        if n == 0:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
    print(s)
    i += 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a2 = []
    a3 = []
    a6 = []
    an = []
    for i in a:
        if i % 6 == 0:
            a6.append(i)
        elif i % 2 == 0:
            a2.append(i)
        elif i % 3 == 0:
            a3.append(i)
        else:
            an.append(i)
    a = a6 + a2 + an + a3
    print(*a)

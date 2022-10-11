
for _ in range(int(input())):
    a = int(input())
    if a == 2:
        print (2, 1)
        continue
    elif a == 3:
        print (-1)
        continue
    n = a
    print(n, n - 1, *range(1, n - 1))


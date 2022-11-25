
for _ in range(int(input())):
    n = int(input())
    if n % 2:
        print('1 ' * n)
    elif n == 2:
        print(1, 3)
    else:
        print('6 ' * (n - 4), 13, 2, 8, 1)


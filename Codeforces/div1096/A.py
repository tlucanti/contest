
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a % 2 and b % 2:
        print('NO')
    else:
        print('YES')

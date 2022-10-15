
for _ in range(int(input())):
    n = int(input())
    if n % 2050 != 0:
        print(-1)
    else:
        print(sum(map(int, str(n // 2050))))



def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(*range(n - 2, 0, -1), n - 1, n)
    else:
        print(n - 1, *range(n - 3, 0, -1), n - 2, n)


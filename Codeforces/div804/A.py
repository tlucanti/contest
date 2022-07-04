
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    if n % 2:
        print(-1)
    else:
        print(0, 0, n // 2)

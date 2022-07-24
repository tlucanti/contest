
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    print(*(list(range(2, n + 1)) + [1]))

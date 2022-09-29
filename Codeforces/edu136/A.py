
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, m = inp()
    print(min(2, n), min(2, m))


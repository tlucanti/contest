
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    m, mi = 0, 0
    for i in range(n):
        if a[i] > m:
            m = a[i]
            mi = i
    print(mi + 1)


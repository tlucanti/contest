
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    a = inp()
    ok = [0] * n
    for i in range(n):
        if a[i] < i + 1:
            ok[i] = 1
    cm = [0] * n
    cm[0] = ok[0]
    for i in range(1, n):
        cm[i] = ok[i] + cm[i - 1]
    ans = 0
    for i in range(2, n):
        if a[i] - 2 < 0 or a[i] - 2 >= n:
            continue
        ans += ok[i] * cm[a[i] - 2]
    print(ans)

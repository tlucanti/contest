
def inp():
    return list(map(int, input().split()))


for _t in range(int(input())):
    n = int(input())
    a = inp()
    ans = 1
    if n == 1:
        print(0)
        continue
    mi = min(a[0], a[1])
    ma = max(a[0], a[1])
    for i in range(2, n):
        if a[i] > ma:
            ma = a[i]
        elif a[i] < mi:
            mi = a[i]
        else:
            ans += 1
            mi = min(a[i], a[i - 1])
            ma = max(a[i], a[i - 1])
    print(ans)

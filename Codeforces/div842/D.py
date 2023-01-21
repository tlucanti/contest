
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    b = sorted(a)

    dif = 0
    for i in range(n):
        if a[i] != b[i]:
            if a[a[i] - 1] == i + 1:
                dif += 1
            else:
                dif += 2
    dif //= 2
    ans = dif + 1

    for i in range(n - 1):
        #print(a[i], a[i + 1], i + 2, i + 1)
        aa = dif
        if a[i] == i + 2:
            di
        if a[i] == i + 2 and a[i + 1] == i + 1:
            ans = min(ans, dif - 2)
        elif a[i] == i + 2:
            ans = min(ans, dif - 1)
        elif a[i + 1] == i + 1:
            ans = min(ans, dif - 1)
    print(max(0, ans))




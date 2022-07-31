
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n, x = inp()
    a = inp()
    ans = 0
    v = [a[0] - x, a[0] + x]
    for i in range(1, n):
        v2 = [a[i] - x, a[i] + x]
        vv = [max(v[0], v2[0]), min(v[1], v2[1])]
        if vv[0] > vv[1]:
            ans += 1
            v = v2
        else:
            v = vv
    print(ans)
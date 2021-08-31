
def check_triangke(a, b, c):
    if a+b <= c or a+c <= b or b+c <= a:
        return 1
    return 0


t = int(input())
for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    ma = max(ar)
    mi = min(ar)
    mai = ar.index(ma)
    mii = ar.index(mi)
    f = 1
    for i in range(n):
        if i == mai or i == mii:
            continue
        if check_triangke(ma, mi, ar[i]):
            f = 0
            break
    if f == 0:
        print(' '.join(map(str, sorted([mai + 1, mii + 1, i + 1]))))
    else:
        print(-1)

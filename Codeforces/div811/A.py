
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n, h, m = inp()
    b = []
    t = h * 60 + m
    for i in range(n):
        hh, mm = inp()
        b.append(hh * 60 + mm)
    b.sort()
    # b.sort(key=lambda x: (x[0], x[1]))_
    ok = False
    for i in range(n):
        if b[i] >= t:
            a = b[i] - t
            ok = True
            break
    if not ok:
        a = b[0] + 60 * 24 - t
    hh = a // 60
    mm = a % 60
    print(hh, mm)

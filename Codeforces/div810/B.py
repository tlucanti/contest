
def inp():
    return list(map(int, input().split()))


def getmin(aa):
    for i in range(len(aa)):
        if fr[aa[i][0]] % 2:
            return aa[i][1]


def getmineven(aa):
    for i in range(len(aa)):
        if fr[aa[i][0]] != 0:
            return i

for _ in range(int(input())):
    n, m = inp()
    a = inp()
    fr = {i: 0 for i in range(n)}
    for i in range(m):
        b = inp()
        fr[b[0] - 1] += 1
        fr[b[1] - 1] += 1
    aa = list(zip(range(n), a))
    aa.sort(key=lambda x: x[1])
    fcnt = sum(fr.values()) // 2
    if fcnt % 2 == 0:
        print(0)
        continue
    ans = 0
    while True:
        mn = getmin(aa)
        if mn is not None:
            ans += mn
            break
        i = getmineven(aa)
        ans += aa[i][1]

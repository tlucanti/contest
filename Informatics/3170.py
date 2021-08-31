a = list(map(int, input().split()))


def fct(n):
    _s = 1
    for _i in range(1, n + 1):
        _s *= _i
    return _s


def cnk(n):
    if n == 0:
        return 0
    return fct(n) // (fct(n - 2) * 2)


for i in range(len(a), 1, -1):
    for j in range(i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

s = 0
ce = a[0]
c = 0
for i in range(len(a)):
    if ce == a[i]:
        c += 1
    else:
        s += cnk(c)
        c = 1
        ce = a[i]
s += cnk(c)
print(s)

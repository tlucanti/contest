
def inp():
    return list(map(int, input().split()))


def argmax(a, start, end):
    m = a[start]
    mi = start
    for i in range(start, end + 1):
        if a[i] > m:
            m = a[i]
            mi = i
    return mi


def argmin(a, start, end):
    m = a[start]
    mi = start
    for i in range(start, end + 1):
        if a[i] < m:
            m = a[i]
            mi = i
    return mi


def req(a, start, end):
    ma, mi = argmax(a, start, end), argmin(a, start, end)
    if {a[start], a[end]} == {a[ma], a[mi]}:
        return 1
    mi, ma = min(mi, ma), max(mi, ma)
    if mi == start:
        low = 0
    else:
        low = req(a, start, mi)
    mid = req(a, mi, ma)
    if ma == end:
        high = 0
    else:
        high = req(a, ma, end)
    return low + mid + high


for _t in range(int(input())):
    n = int(input())
    a = inp()
    if n == 1:
        print(0)
        continue
    print(req(a, 0, n - 1))

def diff(a1, a2):
    s_ = 0
    for z in range(len(a1)):
        if a1[z] != a2[z]:
            s_ += 1
    return s_


n, k = input().split()
n, k = int(n), int(k)
a = list(map(int, input().split()))
s = 0
if k == n:
    print(0)
else:
    for i in range(k):
        _12 = [0, 0]
        for j in range(n // k):
            x = j*k + i
            _12[a[x] - 1] += 1
        s += min(_12)
    print(s)

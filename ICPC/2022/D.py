
import itertools

def inp():
    return list(map(int, input().split()))

def bb(_a):
    return list(map(int, '{:032b}'.format(_a)))

a, b, c = inp()
a = bb(a)
b = bb(b)
c = bb(c)


ans = 0
for p in range(16):
    f0, f1, f2, f3 = list(map(int, '{:04b}'.format(p)))

    aa = [0] * 32
    for i in range(32):
        ii = [a[i], b[i]]
        if ii == [0, 0]:
            aa[i] = f0
        elif ii == [0, 1]:
            aa[i] = f1
        elif ii == [1, 0]:
            aa[i] = f2
        elif ii == [1, 1]:
            aa[i] = f3

    if aa == c:
        ans += 1

print(ans)



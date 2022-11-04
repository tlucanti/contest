
def inp():
    return list(map(int, input().split()))

n, q = inp()
a = inp()
b = [0] * n
c = [0] * n
b[0] = a[0]
c[-1] = a[-1]
for i in range(1, n):
    b[i] = b[i - 1] ^ a[i]
for i in range(q):
    l, r = inp()
    if l - r == 1:


print(a)
print(b)
print(c)


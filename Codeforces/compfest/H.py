
def inp():
    return list(map(int, input().split()))


def f(a, b):
    return (int(str(a) + str(b)) * int(str(b) + str(a)) + a * b) % 3


n = int(input())
a = inp()
b = [i % 3 for i in a]
c = [0, 0, 0] # %0 %1 %2
for i in b:
    c[i] += 1
cc = [c[0], c[1] + c[2]]  # %0 %~0
h = n // 2
if cc[0] == cc[1]:
    table = [h, 0, 0, h]
    z = 0
elif cc[0] > cc[1]:  # %0 > %~0  div3 > !div3
    table = [cc[0] - h, cc[1], h, 0]  # div3, !div3, div3, !div3
    z = 2
else:
    table = [cc[0], cc[1] - h, 0, h]
    z = 0

ans = [0] * n
for i in range(n):
    if a[i] % 3 == 0:
        if table[0] > 0:
            ans[i] = 0
            table[0] -= 1
        else:
            ans[i] = 1
    else:
        if table[1] > 0:
            ans[i] = 0
            table[1] -= 1
        else:
            ans[i] = 1
print(z)
print(*ans, sep='')

def fact(n):
    __s = 1
    for i in range(2, n + 1):
        __s *= i
    return __s


def cnk(n, k):
    return fact(n) // (fact(k) * fact(n - k))


n = int(input())
d = {}
s = set()
ans = 0
for i in range(n):
    a = input()
    d[a[0]] = d.get(a[0], 0) + 1
    s.update(a[0])
for i in s:
    di = d[i]
    ans += cnk(di // 2 + di % 2, 2) + cnk(di // 2, 2)
print(ans)

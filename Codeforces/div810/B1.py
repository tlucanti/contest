
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n, m = inp()
    a = inp()
    inc = [[] for i in range(n)]
    for i in range(m):
        b = inp()
        b[0] -= 1
        b[1] -= 1
        inc[b[0]].append(b[1])
        inc[b[1]].append(b[0])
    if m % 2 == 0:
        print(0)
        continue
    sm = sum(a)
    oddmin = sm
    for i in range(n):
        if len(inc[i]) % 2:
            oddmin = min(oddmin, a[i])
    evenmin = sm
    for i in range(n):
        if len(inc[i]) % 2 == 0:
            for j in inc[i]:
                if len(inc[j]) % 2 == 0:
                    evenmin = min(evenmin, a[i] + a[j])
    print(min(evenmin, oddmin))

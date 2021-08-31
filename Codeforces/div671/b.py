def f(_n):
    return pow(2, _n - 1) * (pow(2, _n) - 1)


t = int(input())
ans = []
for __t in range(t):
    n = int(input())
    s = 0
    a = 1
    i = 0
    while s <= n:
        s += f(i)
        i += 1
    ans.append(str(i - 2))

print('\n'.join(ans))

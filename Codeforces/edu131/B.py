
for _ in range(int(input())):
    n = int(input())
    av = set(range(2, n + 1))
    d = 0
    ans = [0] * n
    ans[0] = 1
    prev = 1
    for i in range(1, n):
        if prev * 2 in av:
            ans[i] = prev * 2
            av.remove(prev * 2)
            prev *= 2
            d += 1
        else:
            m = min(av)
            ans[i] = m
            av.remove(m)
            prev = m
    print(2)
    print(*ans)
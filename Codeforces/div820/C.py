
for i in range(int(input())):
    s = input()
    ss = s
    m = sorted([ord(s[0]), ord(s[-1])])
    s = [(a, i) for (i, a) in enumerate(s) if ord(a) >= m[0] and ord(a) <= m[1]]
    s.sort(key=lambda x: ord(x[0]), reverse=ord(ss[0]) > ord(ss[-1]))
    print(m[1] - m[0], len(s))
    print(*[x[1] + 1 for x in s])


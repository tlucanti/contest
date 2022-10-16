
for _ in range(int(input())):
    n = int(input())
    a = input()
    s = set()
    ans = 0
    for c in a:
        if c not in s:
            ans += 1
            s.add(c)
        ans += 1
    print(ans)


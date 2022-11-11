
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    ok = True
    ans = []
    invs = 0
    if a != b:
        for i in range(n):
            if a[i] != 1 - b[i]:
                ok = False
                break
    else:
        ans.append((1, n))
        for i in range(n):
            a[i] = 1 - a[i]
    if not ok:
        print('NO')
        continue
    print('YES')
    for i in range(n):
        if a[i] == 1:
            ans.append((i + 1, i + 1))
            invs += 1
    if invs % 2 == 0:
        ans.append((1, n))
        ans.append((1, 1))
        ans.append((2, n))
    print(len(ans))
    for i in ans:
        print(*i)



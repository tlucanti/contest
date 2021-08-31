
for t__ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    ans = set()
    f = 1
    for i in range(n):
        if f == 0:
            break
        for j in range(i + 1, n):
            if len(ans) == n - 1:
                f = 0
                break
            if a[i] == a[j]:
                continue
            if not (min(i, j), max(i, j)) in ans:
                ans.update({(min(i, j), max(i, j))})
    if len(ans) == n - 1:
        print('YES')
        for i in ans:
            print(i[0] + 1, i[1] + 1)
    else:
        print('NO')

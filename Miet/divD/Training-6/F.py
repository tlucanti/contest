def dfs(v, nn):
    mm = 0
    for i in mic[v]:
        mm = max(mm, dfs(i, nn + 1))
    return mm + 1


n = int(input())
mic = [[] for i in range(n + 1)]
d = {}
nn = 0
for i in range(n):
    n1, _, n2 = input().split()
    n1 = n1.lower()
    n2 = n2.lower()
    if d.get(n2, -1) == -1:
        d[n2] = nn
        nn += 1
    if d.get(n1, -1) == -1:
        d[n1] = nn
        nn += 1
    mic[d[n2]].append(d[n1])
print(dfs(0, 0))


def dfs(v):
    colors[v] = 1
    for i in inc[v]:
        if colors[i] == 1:
            return i
        if colors[i] == 0:
            ret = dfs(i)
            if ret != -1:
                return ret
    colors[v] = 2
    return -1


n = int(input())
s = list(map(int, input().split()))
inc = [[] for _ in range(n)]
for i in range(n):
    inc[i].append(s[i] - 1)
for i in range(n):
    colors = [0 for _ in range(n)]  # 0 - not visited, 1 - pending, 2 - ended
    print(dfs(i) + 1, end=' ')
print()

def bfs_distance(inc, v, dest):
    if v == dest:
        return 0
    dist = [-1 for _ in range(len(inc))]
    q = [v]
    dist[v] = 0
    while len(q):
        v = q[0]
        q.pop(0)
        for i in inc[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                q.append(i)
            if i == dest:
                return dist[i]
    return -1


n = int(input())
smej = [list(map(int, input().split())) for _ in range(n)]
inc = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if smej[i][j]:
            inc[i].append(j)
a, b = map(int, input().split())
print(bfs_distance(inc, a - 1, b - 1))

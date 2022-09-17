
from collections import deque

INF = int(1e8)


class node():
    def __init__(self, n):
        self.n = n
        self.forward = INF
        self.backward = INF
        self.visited = 0

    def __repr__(self):
        return 'node{' f'{self.n+1, self.forward, self.backward, self.visited}' '}'

    def __str__(self):
        return self.__str__()


class edge():
    def __init__(self, a, b, cost):
        self.a = a
        self.b = b
        self.cost = cost

    def __repr__(self):
        return 'EDGE{' f'{self.a, self.b} cost<{self.cost}>'

    def __str__(self):
        return self.__repr__()


def inp():
    return list(map(int, input().split()))


def bfs_fwd():
    while True:
        if len(q) == 0:
            break
        front = q.popleft()
        front.visited = 1
        for nd in inc[front.n]:
            ed = edges.get((front.n, nd.n), INF)
            nd.forward = min(nd.forward, front.forward + ed)
            if nd.visited:
                continue
            q.append(nodes[nd.n])


def bfs_bwd():
    while True:
        if len(q) == 0:
            break
        front = q.popleft()
        front.visited = 1
        for nd in inc_back[front.n]:
            ed = edges.get((nd.n, front.n), INF)
            nd.backward = min(nd.backward, front.forward + ed, front.backward + ed, nd.forward)
            if nd.visited:
                continue
            q.append(nodes[nd.n])


n, m = inp()

nodes = [0] * n
for i in range(n):
    nodes[i] = node(i)

v = [0] * m
for i in range(m):
    a, b, c = inp()
    a -= 1
    b -= 1
    v[i] = edge(a, b, c)

v.sort(key=lambda x: x.cost)

edges = {(e.a, e.b): e.cost for e in v}
nodes[0].forward = 0
nodes[0].backward = 0

inc = [[] for _ in range(n)]
for i in v:
    inc[i.a].append(nodes[i.b])

inc_back = [[] for _ in range(n)]
for i in v:
    inc_back[i.b].append(nodes[i.a])

q = deque()
q.append(nodes[0])
bfs_fwd()

for _n in nodes:
    _n.visited = 0

q.append(nodes[0])
bfs_bwd()

# print(*inc, sep='\n')
# print()
# print()
# print(nodes)
#
for i in range(1, n):
    b = nodes[i].backward
    if b == INF:
        print(-1, end=' ')
    else:
        print(b, end=' ')
print()

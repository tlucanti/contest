class edge:

    def __init__(self, a, b, cost):
        self.a = a
        self.b = b
        self.cost = cost

    def __repr__(self):
        return f'({self.a}, {self.b}, {self.cost})'


def inp():
    return list(map(int, input().split()))


def ford_bellman(n, m, e, d):
    while True:
        _any = False
        for j in range(m):
            if d[e[j].a] < INF:
                if d[e[j].b] > d[e[j].a] + e[j].cost:
                    d[e[j].b] = d[e[j].a] + e[j].cost
                    _any = True
        if not _any:
            break


e = []
e_reversed = []

INF = int(1e16)

vert, edges = inp()
inc_list = [[] for _ in range(vert)]

for _ in range(edges):
    a, b, cost = inp()
    a -= 1
    b -= 1
    e.append(edge(a, b, cost))

for el in e:
    e_reversed.append(edge(el.b, el.a, el.cost))
    inc_list[el.a].append((el.b, el.cost))

v = 0
d = [INF] * vert
d_reversed = [INF] * vert
d_reversed[v] = 0
d[v] = 0

ford_bellman(vert, edges, e, d)
ford_bellman(vert, edges, e_reversed, d_reversed)

res = []
for num in range(1, vert):
    nm = num
    cur_dist = 0
    while d[nm] >= d_reversed[nm]:
        min_d = d[nm]
        for item in inc_list[num]:
            min_d = min(min_d, d[item[0]] + item[1])
        if min_d == d[nm]:
            break
        for item in inc_list[num]:
            if d[item[0]] + item[1] == min_d:
                cur_dist += item[1]
                nm = item[0]
                break
    if d[nm] == INF:
      res.append(-1)
    else:
      res.append(d[nm] + cur_dist)

print(*res)

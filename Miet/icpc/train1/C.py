
#1-1
#2-1
#3-2
#4-2
#5-3

Dprint = print
Dprint = lambda *_, **__:_

def inp():
    return list(map(int, input().split()))

Y, X, k = inp()
m = [[0] * X for i in range(Y)]
down = [[0] * X for i in range(Y)]
right = [[0] * X for i in range(Y)]

for i in range(k):
    y1, x1, y2, x2 = inp()
    y1 -= 1
    x1 -= 1
    y2 -= 1
    x2 -= 1
    y = min(y1, y2)
    x = min(x1, x2)
    if x1 == x2:
        down[y][x] = 1
    else:
        right[y][x] = 1

for x in range(1, X):
    m[0][x] = m[0][x - 1] + right[0][x - 1]
for y in range(1, Y):
    m[y][0] = m[y - 1][0] + down[y - 1][0]
for y in range(1, Y):
    for x in range(1, X):
        m[y][x] = max(
            m[y - 1][x] + down[y - 1][x],
            m[y][x - 1] + right[y][x - 1]
        )

Dprint(*right, sep='\n')
Dprint()
Dprint(*down, sep='\n')
Dprint()
Dprint(*m, sep='\n')

q = int(input())
for i in range(q):
    yy, xx = inp()
    yy -= 1
    xx -= 1
    mh = (xx + yy + 1) // 2
    ans = 0

    for y in range(Y):
        x = mh - y
        if x > xx or y > yy or x < 0:
            continue
        Dprint(f'ans = max({ans}, m[{y}][{x}] -> {m[y][x]})')
        ans = max(ans, m[y][x])
    print(ans)


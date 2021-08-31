
n, m, r = input().split()
n, m, r = int(n), int(m), int(r)

mat = [[0 for i in range(1000)] for j in range(1000)]
for i in range(n):
    x, y, b = input().split()
    x, y, b = int(x), int(y), int(b)
    mat[x][y] = b


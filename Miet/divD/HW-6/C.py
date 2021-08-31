
def bfs_square(matr, x, y):
    if matr[y][x]:
        return 0
    q = [(x, y)]
    ans = 1
    h = len(matr) - 1
    w = len(matr[0]) - 1
    matr[y][x] = -1
    while len(q):
        x, y = q[0]
        q.pop(0)
        if y < h and matr[y + 1][x] == 0:
            ans += 1
            q.append((x, y + 1))
            matr[y + 1][x] = -1
        if y > 0 and matr[y - 1][x] == 0:
            ans += 1
            q.append((x, y - 1))
            matr[y - 1][x] = -1
        if x < w and matr[y][x + 1] == 0:
            ans += 1
            q.append((x + 1, y))
            matr[y][x + 1] = -1
        if x > 0 and matr[y][x - 1] == 0:
            ans += 1
            q.append((x - 1, y))
            matr[y][x - 1] = -1
    return ans


w, h = map(int, input().split())
matr = [list(map(int, list(input()))) for _ in range(h)]
x, y = map(int, input().split())
print(bfs_square(matr, x - 1, y - 1))

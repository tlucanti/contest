
def inp():
    return list(map(int, input().split()))


n, m = inp()
matr = [input() for i in range(n)]

chars = []
for y in range(n):
    for x in range(m):
        if matr[y][x].isalpha():
            chars.append(matr[y][x])

chars = chars[::-1]

matr = [list(x[::-1]) for x in matr]
matr = matr[::-1]

# print()
# for x in matr:
#     print(''.join(x))

crs = 0
for y in range(n):
    for x in range(m):
        if matr[y][x] == '_':
            matr[y - 1][x] = '_'
            matr[y][x] = '.'
        elif matr[y][x].isalpha():
            matr[y - 1][x] = chars[crs]
            crs += 1
            matr[y][x] = '.'

matr.insert(0, matr[-1])
del matr[-2]

# print()
for x in matr:
    print(''.join(x))


def inp():
    return list(map(int, input().split()))


steps = [None] * 260000
step = 0
n, m = inp()
mp = [list(input()) for i in range(n)]
chars = ('D', 'U', 'R', 'L')

found = False
for y in range(n):
    if found:
        break
    for x in range(m):
        if mp[y][x] == 'S':
            found = True
            sy, sx = y, x
            break

last = 0
steps[last] = (sy + 1, sx, 0)
last += 1
steps[last] = (sy - 1, sx, 1)
last += 1
steps[last] = (sy + 1, sx, 2)
last += 1
steps[last] = (sy + 1, sx, 3)
last += 1

while True:
    if steps[step] is None:
        break
    y, x, char = steps[step]
    if mp[y][x] != '.':
        step += 1
        continue
    mp[y][x] = chars[char]
    steps[last] = (y + 1, x, 0)
    last += 1
    steps[last] = (y - 1, x, 1)
    last += 1
    steps[last] = (y, x + 1, 2)
    last += 1
    steps[last] = (y, x - 1, 3)
    last += 1
    step += 1

for row in mp:
    print(''.join(row))

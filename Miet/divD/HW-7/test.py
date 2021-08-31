
from random import randint as r

with open('input.txt', 'w') as f:
    t = r(100, 100)
    f.write(f'{t}\n')
    mi = 0
    ma = 10
    for i in range(t):
        x1, y1 = r(mi, ma), r(mi, ma)
        x3, y3 = r(mi, ma), r(mi, ma)
        x2, y2 = r(x1, ma), r(y1, ma)
        x4, y4 = r(x3, ma), r(y3, ma)
        f.write(' '.join(map(str, [x1, y1, x2, y2])) + '\n')
        f.write(' '.join(map(str, [x3, y3, x4, y4])) + '\n')

with open('input.txt', 'w') as f:
    f.write(f'{(t:=r(100, 100))}\n')
    for i in range(t):
        l1 = r(-1000, 0)
        r1 = r(l1, 0)

with open('input.txt', 'w') as f:
    f.write(f'{(t:=r(100, 100))}\n')
    for i in range(t):

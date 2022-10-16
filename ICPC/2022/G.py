
import math as m


def search(low, hi, typ):
    while hi - low > 1:
        c = (hi + low) // 2
        print(typ, c, flush=True)
        ans = input()
        if ans == 'in':
            hi = c
        else:
            low = hi
    return low

low = 0
hi = int(1e9) + 1
hi = 100
R2 = search(low, hi, 'E')
low = int(m.floor(m.sqrt(R2)))
hi = int(m.floor(m.sqrt(2 * R2))) + 1
M = search(low, hi, 'M') + 1

sq = int(m.floor(m.sqrt(2*R2 - M*M)))

x = (M + sq) // 2
y = M - x
if x > y or x < 1 or y < 0:
    x = (M - sq) // 2
    y = M - x

print('!', x, y, flush=True)


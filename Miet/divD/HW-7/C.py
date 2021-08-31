
def v_mul(ax, ay, bx, by):
    return ax * by - ay * bx


x1, y1, x2, y2 = map(int, input().split())
x, y = map(int, input().split())

ax = x2 - x1
ay = y2 - y1
bx = x - x1
by = y - y1
s = v_mul(ax, ay, bx, by)
if s == 0:
    print('on line')
elif s < 0:
    print('right')
else:
    print('left')

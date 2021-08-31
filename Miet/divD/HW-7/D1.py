def v_mul(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
l1 = lambda x, y: (y2 - y1) * x + (x2 - x1) * y + x1*y2 - x2*y1
l2 = lambda x, y: (y4 - y3) * x + (x4 - x3) * y + x3*y4 - x4*y3
v1 = (x2 - x1, y2 - y1)
v2 = (x4 - x3, y4 - y3)

if (x1 == x3 and y1 == y3) or \
        (x1 == x4 and y1 == y4) or \
        (x2 == x3 and y2 == y3) or \
        (x2 == x4 and y2 == y4):
    print('yes')
elif v_mul(v1, v2) == 0 and v_mul(v1, (x3 - x1, y3 - y1)) == 0:
    if l2(x1, y1) and (min(x1, x2) < x3 < max(x1, x2) or min(x1, x2) < x4 < max(x1, x2) or
                       min(y1, y2) < y3 < max(y1, y2) or min(y1, y2) < y4 < max(y1, y2)):
        print('yes')
    else:
        print('no')
else:
    a1 = y1 - y2
    b1 = x2 - x1
    c1 = -(x1*y2 - x2*y1)
    a2 = y3 - y4
    b2 = x4 - x3
    c2 = -(x3*y4 - x4*y3)
    d = a1*b2 - a2*b1
    d1 = c1*b2 - c2*b1
    d2 = a1*c2 - a2*c1
    x = d1 / d
    y = d2 / d
    if l1(x, y) == 0 and l2(x, y) == 0:
        print('yes')
    else:
        print('no')


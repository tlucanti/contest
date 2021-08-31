x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
l1 = lambda x, y: (y1 - y2) * x + (x2 - x1) * y + x1*y2 - x2*y1
l2 = lambda x, y: (y3 - y4) * x + (x4 - x3) * y + x3*y4 - x4*y3
if x1 == x2 and y1 == y2:
    if l2(x1, y1) == 0:
        print('yes')
    else:
        print('no')
elif x3 == x4 and y3 == y4:
    if l1(x3, y4) == 0:
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

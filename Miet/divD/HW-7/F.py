from math import sqrt

x1, y1, x2, y2 = map(int, input().split())
x, y = map(int, input().split())
a = pow(x1 - x2, 2) + pow(y1 - y2, 2)
b = pow(x1 - x, 2) + pow(y1 - y, 2)
c = pow(x2 - x, 2) + pow(y2 - y, 2)
if a == 0:
    print(sqrt(b))
elif b == 0 or c == 0:
    print(0)
else:
    cos1 = (a + b - c) / sqrt(2 * a * b)
    cos2 = (a + c - b) / sqrt(2 * a * c)
    if cos1 < 0 or cos2 < 0:
        print(min(sqrt(b), sqrt(c)))
    else:
        print(abs((y2 - y1)*x - (x2 - x1)*y + x2*y1 - y2*x1) / sqrt(a))

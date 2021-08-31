
n = int(input())
if n <= 2:
    print(0)
else:
    x0, y0 = map(int, input().split())
    xx, yy = x0, y0
    s = 0
    for i in range(n - 1):
        x, y = map(int, input().split())
        s += x0*y - x*y0
        x0, y0 = x, y
    s += x*yy - xx*y
    print(abs(s) / 2)
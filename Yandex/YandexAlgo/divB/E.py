def hypot(a, b):
    return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)

d = int(input())
x = list(map(int, input().split()))
a, b, c = (0,0), (d,0), (0,d)
if x[0] > d or x[0] < 0 or x[1] > d or x[1] < 0 or x[0] + x[1] > d:
    dst = [hypot(x,a), hypot(x,b), hypot(x,c)]
    print(dst.index(min(dst)) + 1)
else:
    print(0)

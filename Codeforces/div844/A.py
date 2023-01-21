
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    w, d, h = inp()
    a, b, f, g = inp()
    d1 = a + f + abs(b - g)
    d2 = b + g + abs(a - f)
    d3 = 2*w - a - f + abs(b - g)
    d4 = 2*d - b - g + abs(a - f)
    print(min(d1, d2, d3, d4) + h)




def solve(n):
    v = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    vi = 0
    l = 0
    llast = 1
    second = 0
    c = [0, 0]
    for i in range(n):
        c[0] += v[vi][0]
        c[1] += v[vi][1]
        # print(c)
        l += 1
        if l == llast:
            vi = (vi + 1) % 4
            l = 0
            if not second:
                second = 1
            else:
                llast += 1
                second = 0
    return c


for i in range(100):
    print(i, solve(i))
exit(0)

with open('input.txt', 'r') as f:
    n = int(f.readline())

with open('output.txt', 'w') as f:
    print(*c, file=f)

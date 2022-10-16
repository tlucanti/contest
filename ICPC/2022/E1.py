
def solve(b, c):
    s = set()
    for i in range(b + 1):
        for j in range(c + 1):
            s.add(2 * i + 3 * j)
    return len(s) - 1

for b in range(10):
    for c in range(10):
        ss = solve(b, c)
        sv = 2 * c + b
        print((0, b, c),':', solve(b, c), )

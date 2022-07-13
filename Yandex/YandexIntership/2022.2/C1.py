
def closest_square(n):
    i = 1
    while n not in range(pow(2*i - 1, 2), pow(2*i + 1, 2)):
        i += 1
    return i


def solve(n):
    if n == 0:
        return [0, 0]
    i = closest_square(n)
    pos = n - pow(2*i - 1, 2)
    sq = 2*i * 4
    c = [-i, i - 1]
    if pos in range(0, sq // 4):
        c[1] -= pos
    elif pos in range(sq // 4, sq * 2 // 4):
        c[1] -= sq // 4 - 1
        c[0] += pos - (sq // 4 - 1)
    elif pos in range(sq * 2 // 4, sq * 3 // 4):
        c[1] -= sq // 4 - 1
        c[0] += sq // 4
        c[1] += pos - (sq // 2 - 1)
    else:
        c[1] += 1
        c[0] += sq - pos - 1
    return c


# for i in range(100):
#     print(i, solve(i))
# exit(0)

with open('input.txt', 'r') as f:
    n = int(f.readline())


with open('output.txt', 'w') as f:
    c = solve(n)
    print(*c, file=f)

# closest square search in O(sqrt(n))
# coord search in O(1)
# so algo is O(sqrt(n))


class pair():
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def __getitem__(self, item):
        if item == 0 or item == -2:
            return self.first
        elif item == 1 or item == -1:
            return self.second
        else:
            raise IndexError('Pair has only two items')

    def __eq__(self, other):
        if self.first == other.first and self.second == other.second:
            return True
        else:
            return False

    def __add__(self, other):
        return pair(self.first + other.first, self.second + other.second)

    def __sub__(self, other):
        return pair(self.first - other.first, self.second - other.second)

    def __hash__(self):
        return self.first * 1000 + self.second

    def __repr__(self):
        return '({}, {})'.format(self.first, self.second)


def dist(v1, v2):
    return pow(v1[0] - v2[0], 2) + pow(v1[1] - v2[1], 2)


def check(v1, v2, v3):
    if dist(v1, v2) + dist(v1, v3) == dist(v2, v3) or \
            dist(v1, v3) + dist(v2, v3) == dist(v1, v2) or \
            dist(v1, v2) + dist(v2, v3) == dist(v1, v3):
        return True
    else:
        return False


def not_singular(v1, v2, v3):
    if v1 == v2 or v2 == v3 or v1 == v3:
        return False
    else:
        return True


inp = list(map(int, input().split()))
v1 = pair(inp[0], inp[1])
v2 = pair(inp[2], inp[3])
v3 = pair(inp[4], inp[5])
pairs = [pair(0, 1), pair(1, 0), pair(0, -1), pair(-1, 0)]
f = 0
if check(v1, v2, v3):
    print('RIGHT')
else:
    for i in pairs:
        if (check(v1 + i, v2, v3) and not_singular(v1 + i, v2, v3)) or \
                (check(v1, v2 + i, v3) and not_singular(v1, v2 + i, v3)) or \
                (check(v1, v2, v3 + i) and not_singular(v1, v2, v3 + i)):
            f = 1
            break
    if f:
        print('ALMOST')
    else:
        print('NEITHER')

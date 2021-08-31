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


def v_mul(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


a = pair(*map(int, input().split()))
b = pair(*map(int, input().split()))
c = pair(*map(int, input().split()))
v1 = b - a
v2 = c - a
s = v_mul(v1, v2)
if s < 0:
    print('RIGHT')
elif s > 0:
    print('LEFT')
else:
    print('TOWARDS')
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


def intersection(a, b, c):
    if (a * A[0] + b * A[1] + c) * (a * B[0] + b * B[1] + c) < 0:
        return True
    else:
        return False


A = pair(*map(int, input().split()))
B = pair(*map(int, input().split()))
# v1 = pair(B[0] - A[0], B[1] - A[1])
# a1 = A[1] - B[1]
# b1 = B[0] - A[0]
# c1 = A[0]*B[1] - B[0]*A[1]
# l1 = lambda x, y: a1*x + b1*y + c1
n = int(input())
ans = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if intersection(a, b, c):
        ans += 1
print(ans)

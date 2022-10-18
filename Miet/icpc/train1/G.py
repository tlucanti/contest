
import math as m

EPS = 1e-6

def inp():
    return list(map(int, input().split()))

def dot(a, b):
    return a.x * b.x + a.y * b.y

def cross(a, b):
    return a.x * b.y - a.y * b.x

class vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalize(self):
        l = 1. / self.length()
        self.x *= l
        self.y *= l

    def length(self):
        return m.sqrt(dot(self, self))

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return str((self.x, self.y))

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

for _ in range(int(input())):
    n = int(input())
    v = [vec2(*inp()) for i in range(n)]
    if n == 3:
        print(3)
        print(*v, sep='\n')
    if n % 2 == 0:
        start = 0
        if abs(cross(v[0] - v[1], v[2] - v[3])) == 0:
            start = 1
        ans = []
        for i in range(n // 2):
            p1 = v[(start + 0) % n]
            p2 = v[(start + 1) % n]
            p3 = v[(start + 2) % n]
            p4 = v[(start + 3) % n]
            v1 = p1 - p2
            v2 = p4 - p3
            if dot(v1, v2) > 0:
                ans.append(p2)
                start += 1
            else
                ans.append(intersect_lines(v1, v2))
                start += 2


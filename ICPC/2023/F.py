
import math

def cosd(x):
    return math.cos(math.radians(x))

def Tcos(a, b):
    return math.sqrt(a*a + b*b - 2*a*b*cosd(120))

def heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print('? 0', flush=True)
a = float(input())
print('? 120', flush=True)
b = float(input())
print('? 240', flush=True)
c = float(input())


A = Tcos(a, b)
B = Tcos(b, c)
C = Tcos(c, a)

S = heron(A, B, C)
R = A * B * C / (4 * S)

print(f'! {round(R)}')


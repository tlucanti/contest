
a, b, p, c, n = map(int, input().split())
s = c

for i in range(n):
    c = (c * a + b) % p
    s = (s * c) % p

print(s % p)

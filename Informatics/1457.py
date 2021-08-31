
n, a, b, c, d = map(int, input().split())
s = list(range(1, n + 1))
s[a - 1:b - 1] = s[b - 1:a - 2:-1]
s[c - 1:d - 1] = s[d - 1:c - 2:-1]
print(' '.join(map(str, s)))


import itertools

a, b, c, d = [int(input()) for _ in range(4)]
ans = 0
for p in itertools.permutations((a, b, c, d), 4):
    a, b, c, d = p
    q = c + d
    if a >= q + b or b >= a + q or q >= a + b:
        continue
    if a * d == b * c:
        ans = 1
        break
print(ans)

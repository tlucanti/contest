
def inp():
    return list(map(int, input().split()))

n, a, b = inp()
go = [0] * n
uns = set()
teams = [input().split() for _ in range(n)]
ans = []

for i in range(n):
    if len(uns) >= a:
        break
    if teams[i][0] not in uns:
        uns.add(teams[i][0])
        go[i] = 1

all = a
for i in range(n):
    if all >= a + b:
        break
    if go[i] == 1:
        continue
    go[i] = 1
    all += 1

for i in range(n):
    if go[i]:
        print(' '.join(teams[i]))


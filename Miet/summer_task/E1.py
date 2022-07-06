
def inp():
    return list(map(int, input().split()))


n = int(input())
a_raw = inp()
ones = set()
a = []
for i in range(n):
    if a_raw[i] == 1:
        ones.add(i)
    else:
        a.append([a[i], i])
a.sort(key=lambda x: x[0])

ans = set()
for i in range(n - 1):
    ans.add(sorted([a[i][1], a[i + 1][1]]))
    a[i][0] -= 1
    a[i + 1][0] -= 1

i = 0
j = len(a) - 1
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i][0] == 0:
            break
        if a[j][0] == 0:
            continue
        edge = sorted([a[i][1], a[j][1]])
        if edge not in ans:
            ans.add(edge)
            a[i][0] -= 1
            a[j][0] -= 1

for i in range(len(a)):
    if a[i]
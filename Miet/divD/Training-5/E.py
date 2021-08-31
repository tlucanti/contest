
def count(tab, it):
    ans = 1
    needle = tab[it][1]
    for i in range(it + 1, len(tab)):
        if tab[i][1] == needle:
            ans += 1
        else:
            break
    return ans


n, k = map(int, input().split())
history = [['', [n for i_ in range(k)]] for i in range(n)]
qu = [1 for i_ in range(k)]

for i in range(n):
    s, *q = input().split()
    history[i][0] = s
    for j in range(k):
        if q[j] == '-':
            history[i][1][j] = 0
            qu[j] += 1
        else:
            history[i][1][j] = 1
max_score = 0
for i in range(n):
    sc = 0
    for j in range(k):
        sc += qu[j] * history[i][1][j]
    history[i][1] = sc
    max_score = max(sc, max_score)
history.sort(key=lambda x: x[0])
history.sort(key=lambda x: max_score - x[1])
print(history)
i = 0
while i < n:
    an = count(history, i)
    if an == 1:
        history[i][1] = str(i + 1)
    else:
        for j in range(i, i + an):
            history[j][1] = str(i + 1) + '-' + str(i + an)
    i += an
print(history)
for i in range(n):
    print(history[i][1], history[i][0])


d = {}
history = []
for t__ in range(int(input())):
    s, sc = input().split()
    history.append((s, int(sc)))
    d[s] = d.get(s, 0) + int(sc)
m = max(d.values())
dd = {}
for i in history:
    s, sc = i
    dd[s] = dd.get(s, 0) + sc
    if dd[s] >= m and d[s] == m:
        print(s)
        break

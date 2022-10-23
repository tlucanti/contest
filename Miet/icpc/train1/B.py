
n = int(input())
ok = dict()
att = dict()

for i in range(n):
    ti, ta, v = input().split()
    h, m = ti.split(':')
    t = int(h) * 60 + int(m)
    if ta in ok:
        continue
    if v == 'OK':
        ok[ta] = t
        att[ta] = att.get(ta, 0)
    elif v != 'CE':
        att[ta] = att.get(ta, 0) + 1

ans = 0
for i in ok:
    ans += ok[i] + 20 * att[i]
print(len(ok), ans)


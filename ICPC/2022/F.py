
s = input()
d = dict()
n = len(s)
for c in s:
    d[ord(c)] = d.get(ord(c), 0) + 1

x4 = 0
x2 = 0
x1 = 0
for p in d:
    v = d[p]
    x4 += v // 4
    x2 += v // 2
    x1 += v % 2

#print(d)
#print(x4, x2, x1)
#print()
if x1 > 1:
    print(-1)
else:
    ans = -1
    for w in range(1, n + 1):
        if w * w > n:
            break
        if n % w != 0:
            continue
        h = n // w

        xx4 = (w // 2) * (h // 2)
        xx2 = ((w // 2) * (h % 2) + (h // 2) * (w % 2))
        xx1 = ((w % 2) + (h % 2)) // 2

        xx2 += xx4 * 2
        #print(w, h, ':', xx4, xx2, xx1)
        if xx2 == x2 and xx1 == x1 and xx4 <= x4:
            if ans == -1:
                ans = w + h
            else:
                ans = min(ans, w + h)
    print(ans)


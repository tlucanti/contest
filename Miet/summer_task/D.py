
def inp():
    return list(map(int, input().split()))


def discard(ar, val):
    if val not in ar:
        return
    else:
        ar.remove(val)


n, k = inp()
a = inp()
d = dict()
for i in a:
    d[i] = d.get(i, 0) + 1

ok = True
for key in d:
    if d[key] > k:
        ok = False
        break

if not ok:
    print('NO')
else:
    ans = []
    av = {i: list(range(1, k + 1)) for i in d}
    need = list(range(1, k + 1))
    for i in a:
        if len(need) > 0:
            if need[0] in av[i]:
                ans.append(need[0])
                discard(av[i], need[0])
                del need[0]
        else:
            ans.append(av[i][0])
            del av[i][0]
    if k not in ans:
        print('NO')
    else:
        print('YES')
        print(*ans)



def inp():
    return list(map(int, input().split()))


n = int(input())
a = inp()
ans = []
ok = True
av = [set(range(n)) for i in range(n)]
for i in range(n):
    if not ok:
        break
    while a[i]:
        if len(av[i]) == 0:
            ok = False
            break
        to = av[i].pop()
        if i in av[to]:
            a[i] -= 1
            ans.append(f'{i} {to}')

if ok:
    print('YES')
    print(len(ans))
    print('\n'.join(ans))
else:
    print('NO')

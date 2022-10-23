
a = input()
s = []

mp = {'(':')','[':']','{':'}'}
ok = True
for c in a:
    if c in '([{':
        s.append(c)
    else:
        if len(s) == 0:
            ok = False
            break
        if c == mp.get(s[-1], ''):
            s.pop()
        else:
            ok = False
if len(s) == 0 and ok:
    print('YES')
else:
    print('NO')



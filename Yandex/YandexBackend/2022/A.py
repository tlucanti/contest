
a = list(input())
b = list(input())

pres = [0] * 26
corr = 0

CORRECT = 0
PRESENT = 1
ABSENT = 2

ans = [0] * len(a)

for i in range(len(a)):
    if a[i] == b[i]:
        ans[i] = CORRECT
        a[i] = '0'

for i in range(len(a)):
    if a[i] == '0':
        continue
    ind = ord(b[i]) - ord('A')
    ok = False
    while pres[ind] < len(a):
        if a[pres[ind]] == b[i]:
            ok = True
            pres[ind] += 1
            break
        pres[ind] += 1
    if ok:
        ans[i] = PRESENT
    else:
        ans[i] = ABSENT

tab = ['correct', 'present', 'absent']
for i in ans:
    print(tab[i])

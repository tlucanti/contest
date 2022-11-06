
def add(aa, nn):
    for i in range(len(nn)):
        aa[-i - 1] += nn[-i - 1]


def sub(aa, nn):
    for i in range(len(nn)):
        aa[-i - 1] -= nn[-i - 1]


def poly(aa, sus):
    ans = 0
    for i in range(-size, 0, 1):
        ans = ans * sus + aa[i]
    return ans


s = input()

arr = [0] * int(1e6)
# arr = [0] * int(20)
last = []
inv = False
op = '+'
min_sus = 2
for c in s:
    if c == ' ':
        continue
    elif c.isalnum():
        cc = int(c, 36)
        min_sus = max(min_sus, cc + 1)
        last.append(cc)
        continue

    if op == '+':
        if inv:
            sub(arr, last)
        else:
            add(arr, last)
        last = []
    elif op == '-':
        if inv:
            add(arr, last)
        else:
            sub(arr, last)
        last = []

    if c == '+' or c == '-':
        op = c
    else:
        op = '+'
        inv = True

if op == '+':
    if inv:
        sub(arr, last)
    else:
        add(arr, last)
else:
    if inv:
        add(arr, last)
    else:
        sub(arr, last)


for i in range(len(arr)):
    if arr[i] != 0:
        break
size = len(arr) - i

ok = False
for sus in range(min_sus, 10001):
    if poly(arr, sus) == 0:
        ok = True
        break

if ok:
    print(sus)
else:
    print(-1)



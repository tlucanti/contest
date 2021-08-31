
def index(ar, st):
    for _i in range(len(ar)):
        if ar[_i] == st:
            return _i


def rindex(ar, st):
    for _i in range(len(ar) - 1, -1, -1):
        if ar[_i] == st:
            return _i


n = int(input())
s = input()
d = [0 for i in range(10    )]
for i in range(n):
    a = s[i]
    if a.isdigit():
        d[int(a)] = 0
    elif a == 'L':
        d[index(d, 0)] = 1
    else:
        d[rindex(d, 0)] = 1
print(*d, sep='')


def index(ar, st):
    for _i in range(len(ar)):
        if ar[_i] == st:
            return _i
    return -1


n, k = input().split()
n, k = int(n), int(k)
s = list(map(int, input().split()))
d = []
for i in range(n):
    a = s[i]
    ind = index(d, a)
    if ind == -1:
        d.insert(0, a)
    elif ind >= k:
        d.pop(ind)
        d.insert(0, a)
print(min(k, len(d)))
for i in range(min(k, len(d))):
    print(d[i], end=' ')

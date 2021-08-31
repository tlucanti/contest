
a = list(map(int, input().split()))
mii = 0
mai = 0
mi = a[0]
ma = a[0]
for i in range(len(a)):
    if a[i] < mi:
        mi = a[i]
        mii = i
    elif a[i] > ma:
        ma = a[i]
        mai = i
a[mii], a[mai] = a[mai], a[mii]
print(' '.join(map(str, a)))

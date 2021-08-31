
a = input().split()
n, k = input().split()
n, k = int(n), int(k)
a.append('')
t = 0
for i in range(n, len(a)):
    t = a[i]
    a[i] = k
    k = t
print(' '.join(map(str, a)))

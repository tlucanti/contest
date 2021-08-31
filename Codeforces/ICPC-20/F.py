
s = 0
n = int(input())
a = [0 for i in range(n)]
print("? 1", n)
s = int(input())
sprev = 0
for i in range(2, n):
    print('?', i, n)
    t = int(input())
    a[i - 2] = (s - t) - sprev
    sprev += a[i - 2]
print('?', n-2, n-1)
t2 = int(input())
a[-2] = t2 - a[-3]
a[-1] = t - a[-2]
print('!', ' '.join(map(str, a)))

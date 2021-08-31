
_ = int(input())
a = list(map(int, input().split()))
d = dict()
n = int(input())

for i in range(n - 1):
    m = a[i + 1] - a[i - 1]
    d[m] = d.get(m, set()).update(i)
for i in range(n):
    q, k = input().split()
    k = int(k) - 1
    if q == 'L':
        if a[k - 1] == a[k] - 1:
            print(m[0])
        else:

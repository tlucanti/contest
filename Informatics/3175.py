
n, k = input().split()
n, k = int(n), int(k)
keg = ['I' for i in range(n)]

for b in range(k):
    l, r = input().split()
    l, r = int(l), int(r)
    for j in range(l, r + 1):
        if j > n:
            break
        keg[j - 1] = '.'

print(''.join(keg))

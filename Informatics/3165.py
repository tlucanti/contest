
a = input().split()
for i in range(len(a) // 2):
    a[i * 2], a[i * 2 + 1] = a[i * 2 + 1], a[i * 2]
print(' '.join(a))

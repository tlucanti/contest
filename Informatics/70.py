
n = input()
a = list(map(int, input().split()))
for i in range(len(a) // 2):
    a[2*i], a[2*i + 1] = a[2*i + 1], a[2*i]

print(' '.join(map(str, a)))

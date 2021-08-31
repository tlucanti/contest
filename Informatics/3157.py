
s = 0
a = list(map(int, input().split()))
l = len(a)
for i in range(1, l - 1):
    if a[i-1] < a[i] > a[i+1]:
        s += 1
print(s)
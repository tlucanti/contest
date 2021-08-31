
a = list(map(int, input().split()))
s3 = max(a)
for i in range(4):
    if a[i] != s3:
        print(s3 - a[i], end=' ')

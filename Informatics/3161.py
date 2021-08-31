
a = list(map(int, input().split()))
n = int(input())
i = 0
for i in range(len(a)):
    if a[i] < n:
        break
    i += 1
print(i + 1)

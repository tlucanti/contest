
lst = list(map(int, input().split()))
k = int(input())

for i in range(len(lst)):
    print(lst[(i - k + len(lst) * k) % len(lst)], end=' ')

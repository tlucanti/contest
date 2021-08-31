n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [a[i] - b[i] for i in range(n)]

positive = 0
zeros = 0
for i in range(n):
    if c[i] > 0:
        positive += 1
    elif c[i] == 0:
        zeros += 1
ans = ((positive + zeros) * (positive + zeros - 1) - zeros * (zeros - 1)) // 2
c.sort()

if positive == n:
    print(ans)
elif positive == 0:
    print(0)
else:
    for i in range(n):
        if c[i] >= 0:
            break
    j = i
    i = i - 1
    while i >= 0 and j < n:
        while j < n and abs(c[j]) <= abs(c[i]):
            j += 1
        ans += n - j
        i -= 1
    print(ans)

"""
9
2 8 3 7 2 7 8 5 7
4 5 6 9 5 3 2 5 7   
"""
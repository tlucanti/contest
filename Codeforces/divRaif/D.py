
n = int(input())
a = list(map(int, input().split()))
h = n
last = -1
ans = []
for i in range(n):
    if a[i] != 0:
        if last <= 0:
            ans.append((i + 1, h))
        elif last == 1:
            ans.append((i + 1, h - 1))
        elif last == 2:
            ans.append((i + 1, h + 1))
        elif last == 3:
            ans.append((i + 1, h + 1))
            ans.append((i + 1, h))
        h -= 1
        last = a[i]
if last == 2 or last == 3:
    print(-1)
else:
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

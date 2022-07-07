
def inp():
    return list(map(int, input().split()))


n = int(input())
a = inp()
a = [[a[i], i] for i in range(len(a))]
a.sort(key=lambda x: x[0])
ans = 0
prev = 0
for i in range(0, len(a), 2):
    ans += abs(a[i][1] - prev)
    prev = a[i][1]
prev = 0
for i in range(1, len(a), 2):
    ans += abs(a[i][1] - prev)
    prev = a[i][1]
print(ans)

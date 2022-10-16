
def inp():
    return list(map(int, input().split()))

n, t, c = inp()
a = inp()
s = []
ans = 0
for i in range(n):
    if a[i] > t:
        s.append(i)

if len(s) == 0:
    print(n - c + 1)
else:
    for i in range(1, len(s)):
        if s[i] - s[i - 1] - 1 >= c:
            ans += s[i] - s[i - 1] - c
    if n - s[-1] - 1 >= c:
        ans += n - s[-1] - c
    if s[0] >= c:
        ans += s[0] - c + 1
    print(ans)


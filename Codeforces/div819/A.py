
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    a = inp()
    ma = max(a)
    mi = min(a)
    ans = 0
    for i in a:
        ans = max(ans, i - a[0], a[-1] - i)
    for i in range(1, n):
        ans = max(ans, a[i] - a[i - 1])
    print(ans)
    

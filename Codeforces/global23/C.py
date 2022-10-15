
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    b = [a[i] - a[i - 1] for i in range(1, n)]
    b = [[b[i], i] for i in range(n - 1)]
    #print(b)
    ans = [0] * n
    b.sort(key=lambda x: x[0])
    for i in range(n - 1):
        ans[i] = b[i][1] + 2
    ans[-1] = 1
    print(*(ans[::-1]))


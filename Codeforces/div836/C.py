
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, x = inp()
    if n % x != 0:
        print('-1')
    elif n == x:
        ans = list(range(1, n + 1))
        ans[0] = n
        ans[-1] = 1
        print(*ans)
    else:
        ans = list(range(1, n + 1))
        ans[0] = x
        ans[-1] = 1
        ans[x - 1] = n
        print(*ans)


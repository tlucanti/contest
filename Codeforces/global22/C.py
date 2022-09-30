
def inp():
    return list(map(int, input().split()))


class State():
    def __init__(self, o, e, w):
        self.odd = o
        self.even = e
        self.win = w


for _ in range(int(input())):
    n = int(input())
    a = inp()
    odd = 0
    even = 0
    for i in a:
        if i % 2:
            odd += 1
        else:
            even += 1

    n += 1
    dp = [[None] * n for i in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        dp[i][0] = 1
        dp[0][i] = 1 - dp[0][i - 1]

    for y in range(1, n):
        for x in range(1, n):
            up = dp[y - 1][x]
            left = dp[y][x - 1]

            dp[y][x] = int((not up) or (not left))
    n -= 1
    #if n % 2:
    #    dp[even][odd] = 1 - dp[even][odd]
    #print(*dp, sep='\n')
    #print(even, odd, n)
    if 1:
        up = True
        if even > 0 and dp[even - 1][odd] == 0:
            up = False
        left = True
        if odd > 0 and dp[even][odd - 1] == 0:
            left = False

    if n % 2 == 1:
        if (not up) or (not left):
            print('Bob')
        else:
            print('Alice')
    else:
        if (up or left):
            print('Alice')
        else:
            print('Bob')


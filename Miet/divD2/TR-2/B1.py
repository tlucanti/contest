
def inp():
    return list(map(int, input().split()))

n = int(input())
a = inp()
s = [0] * int(1e6)
for i in a:
    s[i] += 1
dp = []
dp.append(0)
dp.append(s[1])
for i in range(2, int(1e6)):
    dp.append(max(dp[i - 1], dp[i - 2] + s[i] * i))
print(dp[-1])


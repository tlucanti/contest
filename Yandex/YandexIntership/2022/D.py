
n = int(input())
s = list(map(int, input()))

n += 1
dp = [0] * n
z = [0] * n
o = [0] * n
zidx = [0] * n
oidx = [0] * n
n -= 1

print(-1, end='')
for i in range(n):
    i += 1
    dp[i] = dp[i - 1] + (1 if s[i - 1] == 1 else -1)
    o[i] = max(o[i - 1], dp[i])
    z[i] = min(z[i - 1], dp[i])
    if o[i] > o[i - 1]:
        oidx[i] = i
    else:
        oidx[i] = oidx[i - 1]
    if z[i] < z[i - 1]:
        zidx[i] = i
    else:
        zidx[i] = zidx[i - 1]

    if i == 1:
        continue
    if s[i - 1]:
        if z[i - 2] < dp[i]:
            print('', zidx[i - 1] + 1, end='')
        else:
            print(' -1', end='')
    else:
        if o[i - 2] > dp[i]:
            print('', oidx[i - 1] + 1, end='')
        else:
            print(' -1', end='')
print()


import sys
sys.setrecursionlimit(101000)

def inp():
    return tuple(map(int, input().split()))

def dfs(xy):
    #print(xy)
    s[xy] = 1
    for p in (-1, 0), (1, 0), (0, -1), (0, 1):
        pp = (xy[0] + p[0], xy[1] + p[1])
        if pp in s and s[pp] == 0:
            dfs(pp)



n = int(input())
s = {inp() : 0 for _ in range(n)}

groups = 0
for p in s:
    if s[p] == 0:
        dfs(p)
        groups += 1

ans = 1
MOD = 998244353
for i in range(groups):
    ans = (ans * 2) % MOD
#print(groups)
print(ans)


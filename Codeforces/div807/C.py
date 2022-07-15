
def inp():
    return list(map(int, input().split()))


def dfs(a):
    if a < n:
        return a
    else:
        for i in range(len(cc)):
            if a <= cc[i][0][1]:
                b = cc[i][1] + (a - cc[i][0][0])
                return dfs(b)


for _ in range(int(input())):
    n, c, q = inp()
    s = input()
    cc = []
    end = n - 1
    for i in range(c):
        a, b = inp()
        a -= 1
        b -= 1
        cc.append([(end + 1, end + 1 + (b - a)), a])
        end = end + 1 + (b - a)

    for i in range(q):
        ind = int(input()) - 1
        ans = dfs(ind)
        print(s[ans])

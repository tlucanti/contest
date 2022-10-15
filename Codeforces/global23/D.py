def inp():
    return list(map(int, input().split()))

def dfs_max(start):
    mx = 0
    for i in t[start]:
        mx = max(mx, dfs_max(i))
    return mx + s[start]

def dfs_check(start, flag):
    if len(t[start]) > 2:
        return True
    if len(t[start]) == 2:
        if flag:
            return True
        flag = True
    for i in t[start]:
        flag |= dfs_check(i, flag)
    return flag

for _ in range(int(input())):
    n, k = inp()
    a = inp()
    s = inp()
    t = [[] for i in range(n)]
    for i in range(len(a)):
        t[a[i] - 1].append(i + 1)
    branch = False
    for i in start[0]:
        branch |= dfs_check(dfs_check(i))
    if not branch:
        factor = k // len(t[0])
        left = k % len(t[0])
        ans = 0
        scores = []
        for i in t[0]:
            scores.append(dfs_max(i))
        scores.sort(reverse=True)
        for i in scores:
            ans += i * factor
            if left > 0:
                ans += i
                left -= 1
        print(ans + s[0] * k)
    else:



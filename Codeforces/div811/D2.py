
import sys


for _ in range(int(input())):
    t = input()
    n = int(input())
    ss = [input() for __ in range(n)]
    s = set()
    for i in range(len(t)):
        for j in range(n):
            if t[i:].startswith(ss[j]):
                s.add((i, i + len(ss[j]), j))
    s = sorted(s, key=lambda x: (x[0], x[1]))
    # print(len(s))
    end = 0
    i = 0
    ans = []
    while True:
        if end >= len(t):
            break
        if i >= len(s) or s[i][0] > end:
            ans = -1
            break
        for ii in range(i + 1, len(s)):
            if s[ii][0] <= end:
                i = ii
        ans.append((s[i][2] + 1, s[i][0] + 1))
        end = s[i][1]

    if ans == -1:
        print(ans)
    else:
        print(len(ans))
        for i in ans:
            print(*i)

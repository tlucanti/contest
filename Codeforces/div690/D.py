
def solve(n, s):
    cnt = 0
    while 1:
        if len(s) == 1:
            return cnt
        mi = 0
        ma = 0
        for i in range(n):
            if s[i] < s[mi]:
                mi = i
            if s[i] > s[ma]:
                ma = i
        if s[mi] == s[ma]:
            return cnt
        if mi > 0 and mi + 1 < n:
            if s[mi - 1] > s[mi + 1]:
                tt = 1
            else:
                tt = -1
        elif mi > 0:
            tt = -1
        else:
            tt = 1
        s[mi] += s[mi + tt]
        s.pop(mi + tt)
        n -= 1
        cnt += 1


for t in range(int(input())):
    nn = int(input())
    ss = list(map(int, input().split()))
    print(solve(nn, ss))


for _ in range(int(input())):
    n = int(input())
    sa = [input() for _ in range(n)]
    s = set(sa)
    ans = []
    for i in sa:
        ok = False
        for j in range(1, len(i)):
            q1 = i[:j]
            q2 = i[j:]
            if q1 in s and q2 in s:
                ok = True
                break
        if ok:
            ans.append('1')
        else:
            ans.append('0')
    print(''.join(ans))

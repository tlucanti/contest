
for _ in range(int(input())):
    t = input()
    n = int(input())
    sr = [input() for __ in range(n)]
    s = []
    # ss = set()
    for i in range(n):
        if sr[i] in t:
            s.append((sr[i], i))
            # ss |= i
    # if len(ss | set(t)) > len(ss):
    #     print(-1)
    #     continue
    s.sort(key=lambda x: len(x[0]))
    ti = 0
    ans = []
    while True:
        ok = False
        for i in range(len(s)):
            st = s[i][0]
            if t[ti:].startswith(st):
                ans.append((s[i][1] + 1, ti + 1))
                ti += len(st)
                ok = True
                break
        if not ok:
            ans = -1
            break
        if ti >= len(t):
            break
    if ans == -1:
        print(ans)
    else:
        print(len(ans))
        # for aa in ans:
        #     print(*aa)

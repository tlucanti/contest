
for _ in range(int(input())):
    t = input()
    n = int(input())
    sr = [input() for __ in range(n)]
    s = []
    for i in range(n):
        if sr[i] in t:
            s.append((sr[i], i))
    s.sort(key=lambda x: len(x[0]))
    ti = 0
    red = [0] * len(t)
    ans = []
    remaining = len(t)
    if len(s) == 0:
        print(-1)
        continue

    for ti in range(len(t)):
        next = None
        for i in range(len(s)):
            st = s[i][0]
            if t[ti:].startswith(st):
                if next is None:
                    next = s[i][1], ti, get_size(s[i][1], ti, st)
                else:
                    gs = get_size(s[i][1], ti, st)
                    if gs > next[2]:
                        next = s[i][1], ti, gs
                        remaining -= gs
                        for ii in range(len(st)):
                            red[ii + ti] = 1



    while True:
        ok = False
        for i in range(len(s)):
            st = s[i][0]
            if t[ti:].startswith(st):
                ans.append((s[i][1] + 1, ti + 1))
                for j in range(ti, ti + len(st)):
                    if red[j] == 0:
                        remaining -= 1
                    red[j] = 1
                # red[ti:ti + len(st)] = [1] * len(st)
                ti += len(st)
                ok = True
                break
        if not ok:
            ti += 1
        if ti >= len(t):
            break

    if remaining == 0:
        print(len(ans))
        continue

    ti = 0
    while True:
        if red[ti] == 1:
            ti += 1
            continue
        size = 0
        for tti in range(ti, len(red)):
            if red[tti] == 1:
                break
            size += 1

        ok = False
        for ssize in range(size, 0, -1):
            if find_patch(ti, ssize):
                ok = True
                break

        if not ok:
            ans = -1
            break

    print(len(ans), ans, red)
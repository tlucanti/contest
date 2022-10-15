def prt(dd):
    for i in range(ord('a'), ord('z') + 1):
        if i in dd:
            print(chr(i) * dd[i], end='')
    print()


for _ in range(int(input())):
    q = int(input())
    sd = {ord('a'):1}
    td = {ord('a'):1}
    for i in range(q):
        t, k, x = input().split()
        t = int(t)
        k = int(k)

        if t == 1:
            ar = sd
        else:
            ar = td

        for i in x:
            ii = ord(i)
            ar[ii] = ar.get(ii, 0) + k

        # prt(sd)
        # prt(td)
        li = ord('a')
        ti = ord('z')
        while ti not in td:
            ti -= 1
        if ti > li:
            print('YES')
            continue
        # ti == li
        if sd[li] >= td[ti]:
            print('NO')
            continue
        ok = True
        while li <= ord('z'):
            li += 1
            if li in sd:
                ok = False
                break
        if ok:
            print('YES')
        else:
            print('NO')





for t_ in range(int(input())):
    n, m = input().split()
    n, m = int(n), int(m)

    std = dict()
    vtd = [[] for i in range(n)]
    for i in range(n):
        vtd[i] = input().split()
        std[int(vtd[i][0])] = i
    sts = set(std.keys())

    sld = dict()
    vld = [[] for j in range(m)]
    for j in range(m):
        vld[j] = input().split()
        sld[int(vld[j][0])] = j
    sls = set(sld.keys())

    for i in sls:
        if i in sts:
            oo = i
            break

    first = sld[oo]
    for i in range(n):
        st = int(vld[first][i])
        st = std[st]
        print(' '.join(vtd[st]))

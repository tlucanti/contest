
def inp():
    return list(map(int, input().split()))


def compress(a):
    q = a[0]
    n = 0
    ans = []
    for i in a:
        if i == q:
            n += 1
        else:
            ans.append([q, n])
            q = i
            n = 1
    ans.append([q, n])
    return ans


def decompose(a, m):
    def _decomp_one(pp, m):
        if pp[0] % m == 0:
            return _decomp_one([pp[0] // m, pp[1] * m], m)
        else:
            return pp

    for i in range(len(a)):
        a[i] = _decomp_one(a[i], m)


def squeeze(a):
    q = a[0][0]
    n = 0
    ans = []
    for p in a:
        if p[0] == q:
            n += p[1]
        else:
            ans.append((q, n))
            n = p[1]
            q = p[0]
    ans.append((q, n))
    return ans


for _t in range(int(input())):
    n, m = inp()
    a = inp()
    k = int(input())
    b = inp()
    a_comp = compress(a)
    b_comp = compress(b)
    # print(a_comp)
    # print(b_comp)
    decompose(a_comp, m)
    decompose(b_comp, m)
    # print(a_comp)
    # print(b_comp)
    aa = squeeze(a_comp)
    bb = squeeze(b_comp)
    # print(aa)
    # print(bb)

    if aa == bb:
        print('Yes')
    else:
        print('No')
    # print()
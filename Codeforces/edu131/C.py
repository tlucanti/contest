
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n, m = inp()
    a = inp()
    d = dict()
    for i in a:
        d[i] = d.get(i, 0) + 1
    av = set(range(1, n + 1))
    spec = set()
    nonspec1 = set()
    nonspec2 = set()
    ans = 0
    while len(d) > 0:
        ans += 1
        av |= nonspec1
        av |= spec
        nonspec1 = nonspec2
        nonspec2 = set()
        spec = set()
        for i in d:
            if i in av:
                spec.add(i)
                d[i] -= 1
                av.remove(i)
        keys = list(d.keys())
        for i in keys:
            if d[i] == 0:
                del d[i]
        d_nonspec = set(d.keys()) - spec
        for i in av:
            try:
                key = d_nonspec.pop()
                nonspec2.add(i)
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
            except KeyError:
                break
        av -= nonspec2
        for i in av:
            try:
                key = next(iter(d))
                nonspec2.add(i)
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
            except StopIteration:
                break
        av -= nonspec2
    if len(nonspec2) > 0:
        ans += 1
    # elif len(nonspec1) > 0 or len(spec) > 0:
    #     ans += 1
    print(ans)

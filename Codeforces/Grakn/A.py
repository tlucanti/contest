
t = int(input())
for _t in range(t):
    n = int(int(input()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    s = []
    for i in range(n - 1):
        pairs = (a[i + 1], b[i + 1], c[i + 1], a[i - 1], b[i - 1], c[i - 1])
        if not a[i] in pairs:
            s.append(a[i])
        elif not b[i] in pairs:
            s.append(b[i])
        else:
            s.append(c[i])
    print(' '.join(map(str, s)))

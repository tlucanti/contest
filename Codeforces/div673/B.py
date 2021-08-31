
z = int(input())
for i in range(z):
    n, t = input().split()
    n, t = int(n), int(t)
    a = list(map(int, input().split()))
    s = {}
    b = {}

    for j in range(n - 1):
        bg = b.get(a[j], -1)
        if bg == -1:
            b[a[j]] = [1, 1]
        else:
            b[a[j]] = [bg[0] + 1, bg[1] + 1]
        for k in range(j + 1, n):
            if a[j] + a[k] == t:
                s[a[j]] = s.get(a[j], 0) + 1
    j = n - 1
    bg = b.get(a[j], -1)
    if bg == -1:
        b[a[j]] = [1, 1]
    else:
        b[a[j]] = [bg[0] + 1, bg[1] + 1]
    for j in range(n):
        bg = b.get(a[j])
        if s.get(a[j], -1) == -1:
            a[j] = 0
        else:
            if bg[0] > bg[1] // 2:
                b[a[j]][0] -= 1
                a[j] = 1
            else:
                a[j] = 0

    print(' '.join(map(str, a)))

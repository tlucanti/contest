

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    if a[0] != b[0] or a[-1] != b[-1]:
        print(-1)
        continue
    a_borders = []
    b_borders = []

    for i in range(1, n):
        if a[i] != a[i - 1]:
            a_borders.append(i)
        if b[i] != b[i - 1]:
            b_borders.append(i)

    if len(a_borders) != len(b_borders):
        print(-1)
        continue

    ans = 0
    for i in range(len(a_borders)):
        ans += abs(a_borders[i] - b_borders[i])
    print(ans)
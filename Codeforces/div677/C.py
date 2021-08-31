
for t__ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    m = max(s)
    f = False
    for i in range(n):
        if s[i] != m:
            continue
        if i == 0:
            if s[i + 1] != m:
                f = True
                break
        elif i == n - 1:
            if s[i - 1] != m:
                f = True
                break
        else:
            if s[i + 1] != m or s[i - 1] != m:
                f = True
                break
    print(i + 1 if f else -1)

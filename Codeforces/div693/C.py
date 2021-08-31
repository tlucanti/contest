for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    v = [0 for _ in range(n)]
    for i in range(n):
        if s[i] + i < n:
            v[s[i] + i] = max(v[s[i] + i], v[i] + s[i])
        else:
            v[0] = max(v[0], v[i] + s[i])
    print(max(v))

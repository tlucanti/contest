for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    if n < 3:
        print(0)
        continue
    s.sort()
    i = 0
    j = 1
    cnt = 0
    while i < n - 1:
        while j < n - 1:
            if s[j] - s[i] <= 2:
                cnt += j - i - 1
            else:
                break
            j += 1
        if s[j] - s[i] <= 2:
            cnt += j - i - 1
        i += 1
    print(cnt)
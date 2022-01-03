
for t in range(int(input())):
    s = list(input())
    cnt = 0
    for i in range(1, len(s)):
        if i >= 2 and s[i - 2] == s[i]:
            cnt += 1
            s[i] = '_'
        if s[i - 1] == s[i] and s[i] != '_':
            cnt += 1
            s[i] = '_'
    print(cnt)

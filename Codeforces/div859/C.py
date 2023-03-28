
for _ in range(int(input())):
    n = int(input())
    s = input()
    remap = dict()
    remap[s[0]] = '0'
    for i in range(1, n):
        if s[i] in remap:
            continue
        elif remap[s[i - 1]] == '0':
            remap[s[i]] = '1'
        else:
            remap[s[i]] = '0'
    ans = 'YES'
    for i in range(1, n):
        c1 = remap[s[i]]
        c2 = remap[s[i - 1]]
        c = c1 + c2
        if c == '00' or c == '11':
            ans = 'NO'
            break
    print(ans)

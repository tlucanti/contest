
for t in range(int(input())):
    s = input()
    lst = [[s[0], 1]]
    for i in range(1, len(s) - 1):
        if s[i] == lst[-1][0]:
            lst[-1][1] += 1
        else:
            lst.append([s[i], 1])
    if len(s) > 1:
        if s[-1] == lst[-1][0]:
            lst[-1][1] += 1
        else:
            lst.append([s[-1], 1])
    ans = set()
    for i in lst:
        if i[1] % 2:
            ans.update({i[0]})
    print(''.join(sorted(ans)))


for _ in range(int(input())):
    s = input()
    ans = []
    s = s[0].lower() + s[1:]
    i = 1
    while i < len(s):
        if s[i].isupper():
            ans.append(s[:i].lower())
            s = s[i:]
            i = 1
        else:
            i += 1
    if s != '':
        ans.append(s.lower())
    print('_'.join(ans))


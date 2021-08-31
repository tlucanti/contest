
s = input()
d = []
f = 1
for i in range(len(s)):
    a = s[i]
    if len(d) == 0:
        d.append(a)
    elif a == ')':
        if d[-1] == '(':
            d.pop()
        else:
            f = 1
            break
    elif a == ']':
        if d[-1] == '[':
            d.pop()
        else:
            f = 0
            break
    elif a == '}':
        if d[-1] == '{':
            d.pop()
        else:
            f = 0
            break
    else:
        d.append(a)
if len(d) == 0 and f:
    print('Yes')
else:
    print('No')

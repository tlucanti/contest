
n = int(input())
d = []
s = input()
for i in range(n):
    a = s[i]
    if len(d) == 0:
        d.append(a)
    elif a == '(':
        d.append('(')
    elif a == ')':
        if d[-1] == '(':
            d.pop()
        else:
            d.append(')')
if len(d) == 0:
    print('Yes')
elif len(d) == 2:
    if ''.join(d) == ')(':
        print('Yes')
    else:
        print('No')
else:
    print('No')


st = input()
l = len(st)
ma = [0, 0]
mas = 0
jmax = 0
i = 0

while i < l - 1:

    brackets = []
    s = 0
    for j in range(i, l):

        b = st[j]
        if len(brackets) == 0:
            if b in (')', '}', ']'):
                print('wrong', st[i:j + 1])
                break
            else:
                brackets.append(b)
                continue
        if b in ('(', '{', '['):
            brackets.append(b)
            continue
        if b == ')' and brackets[-1] == '(':
            print('correct', st[i:j + 1])
            brackets.pop()
        elif b == '}' and brackets[-1] == '{':
            print('correct', st[i:j + 1])
            brackets.pop()
        elif b == ']' and brackets[-1] == '[':
            print('wrong', st[i:j + 1])
            s += 1
            brackets.pop()
        else:
            print('wrong', st[i:j + 1])
            # brackets.append(b)
            break
        if len(brackets) == 0:
            if s > mas:
                ma = [i, j + 1]
                mas = s
                jmax = max(jmax, j)
            print('correct', st[i:j + 1])
    # print(i, j)
    if j == l - 1:
        i = max(len(brackets), i + 1)
    else:
        i = max(jmax + 1, i + 1)
print(mas)
print(st[ma[0]:ma[1]])

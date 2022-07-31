
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    na, nb = inp()
    a = input()
    b = input()
    if nb > na:
        print('NO')
        continue
    if na == 1:
        if a[0] == b[-1]:
            print('YES')
        else:
            print('NO')
        continue
    if a.endswith(b[1:]):
        if b[0] == '0':
            if '0' in a[:na - nb + 1]:
                print('YES')
            else:
                print('NO')
        else:
            if '1' in a[:na - nb + 1]:
                print('YES')
            else:
                print('NO')
    else:
        print('NO')
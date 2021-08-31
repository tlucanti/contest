
for t in range(int(input())):
    n = int(input())
    s = input()
    if s[:4] == '2020':
        f = 1
    elif s[:3] == '202' and s[-1] == '0':
        f = 1
    elif s[:2] == '20' and s[-2:] == '20':
        f = 1
    elif s[0] == '2' and s[-3:] == '020':
        f = 1
    elif s[-4:] == '2020':
        f = 1
    else:
        f = 0
    print('YES' if f else 'NO')

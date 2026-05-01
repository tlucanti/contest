
for _ in range(int(input())):
    n = int(input())
    s = input()
    if s.count('(') == s.count(')'):
        print('YES')
    else:
        print('NO')

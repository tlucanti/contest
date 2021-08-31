
for q in range(int(input())):
    n = int(input())
    s = [list(map(int, list(input()))),
         list(map(int, list(input())))]
    line = 0
    for i in range(n):
        if s[line][i] >= 3:
            line = 1 - line
            if s[line][i] <= 2:
                line = 0
                break
    print('YES' if line else 'NO')

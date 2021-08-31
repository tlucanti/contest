for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    if s.count(1) % 2 == 0 and s.count(2) % 2 == 0:
        print('YES')
    elif s.count(2) % 2 != 0:
        if s.count(1) >= 2 and s.count(1) % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

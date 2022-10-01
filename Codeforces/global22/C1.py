
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    A = inp()
    a, b = 0, 0
    for i in A:
        if i % 2:
            b += 1
        else:
            a += 1

    if b % 4 == 2:
        print('Bob')
    elif b % 4 == 3:
        print('Alice')
    elif b % 4 == 0:
        print('Alice')
    elif a % 2 == 1:
        print('Alice')
    else:
        print('Bob')


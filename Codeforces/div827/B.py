
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    if len(a) == len(set(a)):
        print('YES')
    else:
        print('NO')

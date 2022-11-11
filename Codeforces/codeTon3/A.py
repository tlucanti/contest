
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    if a[0] != 1:
        print('No')
    else:
        print('Yes')


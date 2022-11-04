
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    m = min(a)
    if m == a[0]:
        print('bob')
    else:
        print('alice')

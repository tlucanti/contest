
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    input()
    n, k = inp()
    a = inp()
    first = dict()
    last = dict()
    for i in range(n):
        if a[i] not in first:
            first[a[i]] = i
        last[a[i]] = i

    for i in range(k):
        a, b = inp()
        if a not in first or b not in first:
            print('NO')
        elif first[a] < last[b]:
            print('YES')
        else:
            print('NO')


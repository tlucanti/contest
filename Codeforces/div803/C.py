
def inp():
    return list(map(int, input().split()))


def solve(a):
    n = len(a)
    s = set(a)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] not in s:
                    return 'NO'
    return 'YES'


for _ in range(int(input())):
    n = int(input())
    a = inp()
    pos, neg, zer = 0, 0, 0
    for i in a:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
    if pos >= 3 or neg >= 3:
        print('NO')
    else:
        a = list(filter(lambda x: x != 0, a))
        if zer > 3:
            zer = 3
        a += [0] * zer

        print(solve(a))

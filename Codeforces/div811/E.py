
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    a = inp()
    _05 = 0
    other = 0
    odd = 0
    even = 0
    for i in range(len(a)):
        if a[i] % 10 == 0:
            _05 += 1
        elif a[i] % 10 == 5:
            _05 += 1
            a[i] += 5
        else:
            other += 1
            while a[i] % 10 != 2:
                a[i] += a[i] % 10
            if (a[i] // 10) % 2:
                odd += 1
            else:
                even += 1

    if _05 != 0:
        if len(set(a)) == 1:
            print('Yes')
        else:
            print('No')
        continue

    if even * odd > 0:
        print('No')
    else:
        print('Yes')
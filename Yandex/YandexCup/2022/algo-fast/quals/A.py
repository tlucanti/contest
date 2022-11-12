
def inp():
    return list(map(int, input().split()))

n, k = inp()
if n == 1 and k == 1:
    print('Yes')
    print(1)
elif n * n % k != 0 or k == 1:
    print('No')
else:
    print('Yes')
    if k > n or n % k != 0:
        c = 0
        for y in range(n):
            for x in range(n):
                print((c % k) + 1, end=' ')
                c += 1
            print()
    else:
        for y in range(n):
            for x in range(n):
                print((x + y) % k + 1, end=' ')
            print()


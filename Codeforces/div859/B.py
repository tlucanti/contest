
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    odd = 0
    even = 0
    for i in a:
        if i % 2:
            odd += i
        else:
            even += i
    if even > odd:
        print('YES')
    else:
        print('NO')

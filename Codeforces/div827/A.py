
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    a, b, c = inp()
    if a == b + c or b == a + c or c == b + a:
        print('YES')
    else:
        print('NO')

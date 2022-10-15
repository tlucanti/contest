
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, k = inp()
    a = inp()
    print('YES' if 1 in a else 'NO')


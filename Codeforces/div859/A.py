
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    a, b, c = inp()
    if a + b == c:
        print('+')
    else:
        print('-')


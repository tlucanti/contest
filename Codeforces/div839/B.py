
def inp():
    return list(map(int, input().split()))

def check(a, b, c, d):
    return a < b and c < d and a < c and b < d

for _ in range(int(input())):
    a, b = inp()
    c, d = inp()
    ans = 'NO'
    for i in range(4):
        if check(a, b, c, d):
            ans = 'YES'
            break
        a, b, c, d = c, a, d, b
    print(ans)


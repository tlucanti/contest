
def inp():
    return list(map(int, input().split()))

def solve(a):
    r = a[0] % 2
    ans = 0
    for i in range(1, len(a)):
        if a[i] % 2 != r:
            r = 1 - r
        else:
            ans += 1
    return ans

for _ in range(int(input())):
    n = int(input())
    a = inp()
    print(solve(a))

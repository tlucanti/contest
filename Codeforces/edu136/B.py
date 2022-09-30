
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    s = [0] * n
    s[0] = a[0]
    for i in range(1, n):
        if s[i - 1] - a[i] < 0 or a[i] == 0:
            s[i] = s[i - 1] + a[i]
        else:
            s = [-1]
            break
    print(*s)



def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    s = inp()
    a = [input().split()[1] for _ in range(n)]
    for i in range(n):
        u = a[i].count('U')
        d = a[i].count('D')
        print((s[i] - u + d) % 10, end=' ')
    print()
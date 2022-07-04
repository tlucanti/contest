
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n, m = inp()
    ans = []
    for i in range(n):
        if i % 2:
            ans.append('1001' * (m // 2))
            ans.append('1001' * (m // 2))
        else:
            ans.append('0110' * (m // 2))
            ans.append('0110' * (m // 2))
    ans = ans[1:]
    for i in range(n):
        line = ans[i][:m]
        print(' '.join(line))

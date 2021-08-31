
for t in range(int(input())):
    n = int(input())
    inc = [[] for _ in range(n)]
    w = list(map(int, input().split()))
    wei = []
    colors = [0 for _ in range(n - 1)]
    ans = [0 for _ in range(n - 1)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        wei.append([a, b, w[a], w[b]])
        inc[a].append(b)
        inc[b].append(a)
        colors[i] = w[a] + w[b]
    wei.sort(key=lambda x: x[2] + x[3])
    ans[0] = sum(colors)
    for i in range(1, n - 1):
        if wei[i - 1][2] + wei[i - 1][3] == 0:
            print("ERROR")
        elif wei[i - 1][2] != 0 and wei[i - 1][3] != 0:
            minus = min(wei[i - 1][2], wei[i - 1][3])
            if wei[i - 1][2] == minus:
                wei[i - 1][0] = 0
            else:
                wei[i - 1][1] = 0
        elif wei[i - 1][2] != 0:
            minus = wei[i - 1][2]
            wei[i - 1][0] = 0
        else:
            minus = wei[i - 1][3]
            wei[i - 1][1] = 0
        ans[i] = ans[i - 1] - minus
    # ans[n - 2] = sum(w)
    print(*ans[::-1])

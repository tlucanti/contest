def dfs(n):
    global cnt
    arr[n][0] = cnt
    for i in matr[n]:
        cnt += 1
        dfs(i)
    arr[n][1] = cnt


cnt = 0
n = int(input())
matr = [[] for _ in range(n)]
arr = [[0, 0] for _ in range(n)]
s = list(map(int, input().split()))
root = 0
for i in range(n):
    a, b = i, s[i] - 1
    if b == -1:
        root = i
        continue
    matr[b].append(a)

dfs(root)
for i in range(int(input())):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    a, b = b, a
    if arr[b][0] <= arr[a][0] <= arr[b][1]:
        print(1)
    else:
        print(0)

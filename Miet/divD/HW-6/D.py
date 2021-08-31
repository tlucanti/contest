
global stack, colors

inp = open('input.txt', 'r')
out = open('output.txt', 'w')
input = inp.readline
print = lambda *x: out.write(' '.join(map(str, x)) + '\n')


def dfs_cycle(v):
    colors[v] = 1
    stack.append(v)
    for i in inc[v]:
        if colors[i] == 1:
            stack.append(i)
            return stack
        if colors[i] == 0:
            ret = dfs_cycle(i)
            if ret != -1:
                return ret
    colors[v] = 2
    stack.pop()
    return -1


for t in range(int(input())):
    n, m = map(int, input().split())
    inc = [[] for i in range(n)]
    f = 0
    ans = -1
    for i in range(m):
        a, b = map(int, input().split())
        if a == b:
            f = a
        inc[a - 1].append(b - 1)
    if not f:
        stack = []
        colors = [0 for i in range(n)]  # 0 - not visited, 1 - pending, 2 - ended
        for i in range(n):
            if colors[i] == 0:
                ans = dfs_cycle(i)
                if ans != -1:
                    break
        if ans == -1:
            print("NO")
        else:
            print("YES")
            # print("ANS >> ", ans)
            vv = ans[-1] + 1
            i = 0
            for i in range(len(ans) - 2, -1, -1):
                ans[i] += 1
                if ans[i] == vv:
                    break
            print(*ans[i:-1])
    else:
        print("YES")
        print(f)

inp.close()
out.close()

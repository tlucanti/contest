
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        print(1, 2)
        continue
    ans = []
    l = 1
    r = 3 * n
    while l < r:
        ans.append((l, r))
        l += 3
        r -= 3
    print(len(ans))
    for i in ans:
        print(*i)


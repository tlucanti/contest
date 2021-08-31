
for t__ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    block_list = list(map(int, input().split()))
    # open_num = n - sum(block_list)
    open_list = []
    for i in range(n):
        if not block_list[i]:
            open_list.append(a[i])
    open_list = list(reversed(sorted(open_list)))
    j = 0
    for i in range(n):
        if not block_list[i]:
            a[i] = open_list[j]
            j += 1
    for i in range(n):
        print(a[i], end=' ')
    print()

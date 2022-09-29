
for _ in range(int(input())):
    a = list(map(int, input()))
    n = len(a)
    last = [0] * 10
    for i in range(n):
        last[a[i]] = i
    for i in range(1, 10):
        last[i] = max(last[i], last[i - 1])

    cnt = [0] * 10
    #print(last)
    for i in range(n):
        if a[i] == 0:
            cnt[0] += 1
            continue
        if last[a[i] - 1] > i:
            cnt[min(9, a[i] + 1)] += 1
        else:
            cnt[a[i]] += 1
    for i in range(10):
        print(str(i) * cnt[i], end='')
    print()

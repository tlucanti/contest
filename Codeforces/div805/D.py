
for _ in range(int(input())):
    a = input()
    p = int(input())
    cost = sum([ord(x) - ord('a') + 1 for x in a])
    deleted = [0] * 26
    ps = sorted(a, reverse=True)
    for c in ps:
        if cost <= p:
            break
        else:
            cc = ord(c) - ord('a')
            deleted[cc] += 1
            cost -= cc + 1
    for c in a:
        cc = ord(c) - ord('a')
        if deleted[cc] > 0:
            deleted[cc] -= 1
            continue
        else:
            print(c, end='')
    print()

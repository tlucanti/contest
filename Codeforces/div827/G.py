def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    AA = inp()
    aa = [[AA[i], i] for i in range(n)]
    aa.sort(reverse=True)

    mp = [[-1] * 32 for i in range(32)]
    for i in range(n):
        b = list(map(int, '{:032b}'.format(aa[i][0])))
        start = 0
        while start < len(b):
            if b[start] == 1:
                for end in range(start, len(b)):
                    if b[end] == 0:
                        end -= 1
                        break
                if mp[start][end] == -1:
                    mp[start][end] = aa[i][1]
                start = end
            start += 1

    bits = [0] * 32
    used = [0] * n
    first = True

    del i
    start = 0
    end = 31
    while start < 32:
        while end >= start:
            num = mp[start][end];
            if num == -1:
                end -= 1
                continue
            if used[num] == 1:
                end -= 1
                continue
            print(AA[num], end=' ')
            used[num] = 1
            b = list(map(int, '{:032b}'.format(AA[num])))
            for i in range(32):
                bits[i] = b[i]
            del i
            if first:
                for i in range(32):
                    if bits[i] == 1:
                        break
                    bits[i] = 1
                del i
            first = False
            start = 32
            for i in range(32):
                if bits[i] == 0:
                    start = i - 1
                    break
            del i
            break
        start += 1
        end = 31

    for i in range(n):
        if used[i] == 0:
            print(AA[i], end=' ')
    print()



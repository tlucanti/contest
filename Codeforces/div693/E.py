
def srt(ar, key):
    for i in range(len(ar) - 1):
        for j in range(len(ar) - i - 1):
            if key(ar[j]) >= key(ar[j + 1]):
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
                ind[j], ind[j + 1] = ind[j + 1], ind[j]
    return ar


for t in range(int(input())):
    n = int(input())
    s = []
    ind = [_ // 2 for _ in range(n * 2)]
    for i in range(n):
        a, b = map(int, input().split())
        s.append((a, b, i))
        s.append((b, a, i))
    s = srt(s, key=lambda x: x[1])
    s = srt(s, key=lambda x: x[0])
    s = s[::-1]
    # s.sort(key=lambda x: x[0])
    # s.sort(key=lambda x: x[1])
    print(s)
    print(ind)
    # for i in range(n * 2):
    #     if ind[i] < n * 2 - 1 and ind
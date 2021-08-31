
for t in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    a = 0
    # if n <= 2:
    #     print(sum(s[::n]))
    #     continue
    for i in range(k):
        a += s[-(n//2 + 1) - i*(n//2 + 1)]
    print(a)

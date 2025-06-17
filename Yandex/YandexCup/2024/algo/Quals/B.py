
for t in range(int(input())):
    n = int(input())
    h = [int(x) for x in input().split()]

    if n < 3:
        print(0)
        continue

    ans = 0
    for c in range(1, n - 1):
        if h[c] > h[c - 1] and h[c] > h[c + 1]:
            l = c
            while l - 1 >= 0 and h[l - 1] < h[l]:
                l -= 1
            r = c
            while r + 1 < n and h[r + 1] < h[r]:
                r += 1
            ans += (c - l) * (r - c)
    print(ans)




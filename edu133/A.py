
for _ in range(int(input())):
    n = int(input())
    ans = 0
    if n >= 4 and (n - 4) % 3 == 0:
        n -= 4
        ans += 2
    ans += n // 3
    n = n % 3
    if n == 1:
        ans += 2
    elif n == 2:
        ans += 1
    print(ans)

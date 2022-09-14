
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input()))

    i = n - 1
    ans = ''
    while i >= 0:
        if s[i] == 0:
            ans += chr(ord('a') - 1 + s[i - 2] * 10 + s[i - 1])
            i -= 3
        else:
            ans += chr(ord('a') - 1 + s[i])
            i -= 1
    print(ans[::-1])


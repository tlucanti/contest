
for t__ in range(int(input())):
    n = int(input())
    a = input()
    b = set(a)
    if '>' in a and '<' in a:
        ans = 0
        for i in range(n):
            if a[i] == '-' or a[i - 1] == '-':
                ans += 1
        print(ans)
    else:
        print(n)

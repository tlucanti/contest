
for _ in range(int(input())):
    s = int(input())
    ans = ''
    next = 9
    while s > 0:
        if s > next:
            ans = str(next) + ans
            s -= next
            next -= 1
        else:
            ans = str(s) + ans
            s = 0

    print(ans)
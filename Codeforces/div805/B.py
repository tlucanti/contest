
for _ in range(int(input())):
    a = input()
    s = set()
    ans = 0
    for i in a:
        if i in s:
            continue
        else:
            if len(s) == 3:
                ans += 1
                s = {i}
            else:
                s.add(i)
    print(ans + 1)


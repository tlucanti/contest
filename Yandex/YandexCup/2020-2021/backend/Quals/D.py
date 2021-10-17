from sys import stdout

n = int(input())
l = 0
r = n
i = 1

while i < n:
    print((l + r) // 2)
    stdout.flush()
    d = int(input())
    if (l + r) // 2 == 1:
        if d == 0:
            r = 1
            break
    if d == 1:
        l = (l + r) // 2
    else:
        r = (l + r) // 2
    i *= 2
print('!', r)
# 795485
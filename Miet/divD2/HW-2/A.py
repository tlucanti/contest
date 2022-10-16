
n = int(input())
s = input()
a = [0] * 10
for c in s:
    if c == 'L':
        for i in range(10):
            if a[i] == 0:
                a[i] = 1
                break
    elif c == 'R':
        for i in range(9, -1, -1):
            if a[i] == 0:
                a[i] = 1
                break
    else:
        a[int(c)] = 0
print(*a, sep='')


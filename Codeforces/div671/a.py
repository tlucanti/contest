
t = int(input())
ans = []
for j in range(t):
    n = int(input())
    a = input()
    f = 0
    i = 1
    if n % 2 == 0:
        for i in range(1, n, 2):
            if int(a[i]) % 2 == 0:
                f = 1
                break
        if f == 1:
            ans.append('2')
        else:
            ans.append('1')
    else:
        for i in range(0, n, 2):
            if int(a[i]) % 2 == 1:
                f = 1
                break
        if f == 1:
            ans.append('1')
        else:
            ans.append('2')
print('\n'.join(ans))

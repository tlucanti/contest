
n, k = input().split()
n, k = int(n), int(k)

if n == 4 and k == 3:
    print('Yes')
elif k == 2:
    if n % 2 == 0:
        print('Yes')
    else:
        print('No')
elif k == 1:
    print('Yes')
else:
    print('No')


a = input().split()
z = 0

for i in range(len(a)):
    if int(a[i]) == 0:
        z += 1
    else:
        print(a[i], end=' ')

for i in range(z):
    print('0 ', end='')

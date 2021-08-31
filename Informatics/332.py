
n = int(input())
array = []
for i in range(n):
    a = input().split()
    array.append([a[0] + ' ' + a[1], int(a[2]) + int(a[3]) + int(a[4])])

array.sort(key=lambda x: 15 - x[1])

for i in range(n):
    print(array[i][0])
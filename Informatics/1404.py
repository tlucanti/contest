
n = int(input())
array = []

for i in range(n):
    sur, nam, cla, dat = [input() for __i in range(4)]
    array.append([cla, sur, nam, dat, cla])
    if len(cla) == 2:
        array[-1][-1] = '0' + array[-1][-1]

array.sort(key=lambda x: x[1])
array.sort(key=lambda x: x[-1])

for i in range(n):
    print(array[i][0], array[i][1], array[i][2], array[i][3])

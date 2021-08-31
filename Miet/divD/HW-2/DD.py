def shaker_sort(arr):
    beg = 0
    end = len(arr)
    while beg < end:
        for i in range(beg, end - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        for i in range(end - 1, beg, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        beg += 1
        end -= 1
    return arr


p = list(map(int, input().split(',')))
l = len(p)
if l == 1:
    print(p[0])
else:
    shaker_sort(p)
    start = p[0]
    end = p[0]
    first = True
    for i in range(1, l):
        if p[i] - p[i - 1] <= 1:
            end = p[i]
        else:
            if start == end:
                if not first:
                    print(',', end='')
                else:
                    first = False
                print(start, end='')
            else:
                if not first:
                    print(',', end='')
                else:
                    first = False
                print(start, '-', end, sep='', end='')
            start = p[i]
            end = p[i]
    if p[-1] - p[-2] <= 1:
        end = p[-1]
    if start == end:
        if not first:
            print(',', end='')
        else:
            first = False
        print(start, end='')
    else:
        if not first:
            print(',', end='')
        else:
            first = False
        print(start, '-', end, sep='', end='')
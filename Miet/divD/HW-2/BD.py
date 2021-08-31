def comb_sort(arr):
    l = len(arr)
    falen = l
    while 1:
        falen = falen / 1.2473309
        alen = int(falen)
        for i in range(l - alen):
            if arr[i] > arr[i + alen]:
                arr[i], arr[i + alen] = arr[i + alen], arr[i]
        if alen <= 1:
            break
        for i in range(l - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1], = arr[i + 1], arr[i]
    return arr


for t__ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    comb_sort(a)
    for i in range(n // 2 - (n + 1) % 2):
        print(a[n // 2 - i - (n + 1) % 2], end=' ')
        print(a[n // 2 + i + n % 2], end=' ')
    print(a[0], end=' ')
    if n % 2 == 0:
        print(a[-1], end=' ')
    print()

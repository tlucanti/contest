def bubble_sort(arr):
    sorted_ = True
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_ = False
        if sorted_:
            break
    return arr


for t__ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    bubble_sort(a)
    f = True
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            f = False
            break
    print('YES' if f else 'NO')

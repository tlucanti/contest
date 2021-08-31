def w_sort(arr, p):
    # sorted_ = True
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1] and ((j + 1) in p):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # sorted_ = False
        # if sorted_:
        #     break
    return arr


def issorted(a):
    for i in range(1, len(a)):
        if not a[i - 1] <= a[i]:
            return 0
    return 1


for t__ in range(int(input())):
    n, m = input().split()
    n, m = int(n), int(m)

    a = list(map(int, input().split()))
    p = set(map(int, input().split()))
    w_sort(a, p)
    if issorted(a):
        print("YES")
    else:
        print("NO")

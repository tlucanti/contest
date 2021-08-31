def bin_search(arr, item):
    l = len(arr)
    j = l // 2
    while 1:
        if arr[j][0] <= item <= arr[j][1]:
            return j + 1
        if item < arr[j][0]:
            j //= 2
        else:
            j += j // 2


n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
qq = [[0, 0] for i in range(n)]
qq[0] = [1, a[0]]
for i in range(1, n):
    qq[i] = [qq[i - 1][1] + 1, qq[i - 1][1] + a[i]]
for i in q:
    print(bin_search(qq, i))

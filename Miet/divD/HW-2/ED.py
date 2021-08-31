def gnome_sort(arr):
    i = 0
    l = len(arr)
    while i < l:
        if i == 0:
            i += 1
        else:
            if arr[i - 1] <= arr[i]:
                i += 1
            else:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                i -= 1
    return arr


n, m = input().split()
n, m = int(n), int(m)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mi = m + 1
gnome_sort(a)
gnome_sort(b)
for i in range(n):
    ss = [(m - a[__i] + b[(__i + i) % n]) % m for __i in range(n)]
    if ss.count(ss[0]) == n:
        mi = min(mi, ss[0])
print(mi)

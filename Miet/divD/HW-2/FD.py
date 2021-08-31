def selection_sort(arr):
    for i in range(len(arr)):
        mi = i
        for j in range(i, len(arr)):
            if arr[j] < arr[mi]:
                mi = j
        arr[mi], arr[i] = arr[i], arr[mi]
    return arr


print("YES" if selection_sort(list(input() + input())) == selection_sort(list(input())) else "NO")

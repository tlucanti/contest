def selection_sort(arr):
    for i in range(len(arr)):
        mi = i
        for j in range(i, len(arr)):
            if arr[j] < arr[mi]:
                mi = j
        arr[mi], arr[i] = arr[i], arr[mi]
    return arr


n = int(input())
a = list(map(int, input().split()))
print(' '.join(map(str, selection_sort(a))))


# def sort_test(_arr):
#     for i in range(len(_arr) - 1):
#         if not _arr[i] <= _arr[i + 1]:
#             print()
#             print(i, end='::')
#             return 1
#     return 0
#
#
# import random
# for i in range(10):
#     a = [random.randint(1, 1000) for j in range(random.randint(1, 10000))]
#     # print(a)
#     b = a.copy()
#     a = selection_sort(a)
#     if sort_test(a):
#         print('wrong', b)
#         print('     ', a)
#     else:
#         print('.', end='')


def bubble_sort(arr):
    sorted_ = True
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j][0] < arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_ = False
        if sorted_:
            break
    return arr


def summ(s):
    ans = 0
    for i in s:
        ans += int(i)
    return ans


n = int(input())
a = input().split()
b = []
for i in range(n):
    b.append([summ(a[i]), a[i]])
bubble_sort(b)
for i in range(n):
    print(b[i][1], end=' ')
print()

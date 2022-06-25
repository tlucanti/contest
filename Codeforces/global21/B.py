
def inp():
    return list(map(int, input().split()))


for _t in range(int(input())):
    n = int(input())
    a = inp()
    if set(a) == {0}:
        print(0)
        continue
    i = 0
    for i in range(n):
        if a[i] != 0:
            break
    j = n - 1
    for j in range(n - 1, -1, -1):
        if a[j] != 0:
            break
    a = a[i:j + 1]
    if 0 in a:
        print(2)
    else:
        print(1)


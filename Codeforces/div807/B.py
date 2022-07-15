
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    a = inp()[:-1]
    for i in range(len(a)):
        if a[i] != 0:
            a = a[i:]
            break
    if sum(a) == 0:
        print(0)
    else:
        print(sum(a) + a.count(0))

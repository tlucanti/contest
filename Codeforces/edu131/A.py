
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    l1 = inp()
    l2 = inp()
    a = l1 + l2
    if a.count(1) == 0:
        print(0)
    elif a.count(1) == 4:
        print(2)
    else:
        print(1)



def inp():
    return list(map(int, input().split()))

def rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

for _ in range(int(input())):
    n = int(input())
    a = inp()
    if set(a) == {1} or set(a) == {0}:
        print(0)
        continue
    first_1 = a.index(1)
    last_0 = rindex(a, 0)
    ans = 0
    while first_1 < last_0:
        ans += 1
        a[first_1] = 0
        first_1 += 1
        a[last_0] = 1
        last_0 -= 1
        while first_1 < n and a[first_1] == 0:
            first_1 += 1
        while last_0 >= 0 and a[last_0] == 1:
            last_0 -= 1
    print(ans)

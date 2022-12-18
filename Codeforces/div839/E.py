
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = inp()
    f, s, same = 0, 0, 0
    for i in range(n):
        if a[i] != i + 1 and a[i] != n - i:
            same += 1
        if a[i] != i + 1:
            f += 1
        if a[i] != n - i:
            s += 1
    print(f, s, same)

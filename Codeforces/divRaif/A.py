
for t__ in range(int(input())):
    a = list(map(int, input().split()))
    print(abs(a[0] - a[2]) + abs(a[1] - a[3]) + (a[0] != a[2] and a[1] != a[3]) * 2)

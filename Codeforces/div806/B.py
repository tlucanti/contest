
def inp():
    return list(map(int, input().split()))


for _ in range(int(input())):
    n = int(input())
    a = input()
    s = set()
    ans = 0
    for i in a:
        if i in s:
            ans += 1
        else:
            ans += 2
            s.add(i)
    print(ans)

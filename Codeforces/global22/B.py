
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, k = inp()
    a = inp()
    last = None
    ans = 'YES'
    for i in range(k - 2, -1, -1):
        e = a[i + 1] - a[i]
        if last is not None and e > last:
            ans = 'NO'
            break
        last = e

    if k > 1 and (n - k + 1) * last < a[0]:
        ans = 'NO'
    print(ans)


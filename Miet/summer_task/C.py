

def inp():
    return list(map(int, input().split()))


n, k = inp()
a = inp()
if k == 1:
    print(n - n % 2)
else:
    d = dict()
    for i in a:
        d[i % k] = d.get(i % k, 0) + 1

    ans = 0
    for key in d:
        if key == 0:
            ans += (d[key] - d[key] % 2)
        elif key == k - key:
            ans += d[key] - d[key] % 2
        else:
            ans += min(d[key], d.get(k - key, 0))

    print(ans)

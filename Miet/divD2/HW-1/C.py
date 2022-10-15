
def inp():
    return list(map(int, input().split()))

n, k = inp()
h = n // 2 + n % 2
if k <= h:
    print(2 * k - 1)
else:
    print(2 * (k - h))


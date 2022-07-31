
def inp():
    return list(map(int, input().split()))


def convolve()

for _ in range(int(input())):
    n, m = inp()
    prev = inp()
    p = list(prev)
    for i in range(n - 1):
        a = inp()
        dif = [abs(i - j) for i, j in zip(a, prev)]
        print(*dif)
        prev = a
    print(*[abs(i - j) for i, j in zip(a, p)])

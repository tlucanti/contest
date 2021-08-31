
def f(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def ank(n, k):
    return f(k) // f(k - n)


def cnk(n, k):
    return f(k) // (f(n) * f(k - n))


n = int(input())
print(ank(n // 2, n) // (n // 2) * ank(n // 2, n // 2) // (n // 2) // 2)

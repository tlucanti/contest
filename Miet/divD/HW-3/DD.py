# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


def factor(a):
    f = []
    a_ = a
    not_prime = True
    while not_prime:
        not_prime = False
        i = 2
        while i * i <= a:
            if a % i == 0:
                f.append(i)
                a //= i
                not_prime = True
                break
            i += 1
    if a_ == a:
        return []
    f.append(a)
    return f


def euler_func(n):
    s = n
    if n in {0, 1}:
        return n
    f = set(factor(n))
    if len(f) == 0:
        return n - 1
    for p in f:
        s *= (p - 1)
    for p in f:
        s //= p
    return s


# def next_set(ar, n):
#     for i in range(len(ar) - 1, -1, -1):
#         if ar[i] < n:
#             ar[i] += 1
#             for j in range(i + 1, len(ar)):
#                 ar[j] = ar[i]
#             return True
#     return False


# def arr_mask_mul(ar, mask):
#     s = 1
#     for i in mask:
#         if i == 0:
#             continue
#         s *= ar[i - 1]
#     return s


def reseto(mmax, find_primes):
    ar = {0, 1}
    left_primes = mmax - 1
    for i in find_primes:
        for j in range(i, mmax + 1, i):
            if j not in ar:
                left_primes -= 1
                ar.update({j})
    return left_primes


# def fast_not_work(n): # O(sqrt(n))
#     f = factor(n)
#     ans = 0
#     fn = len(f)
#     if n == 1 or n == 0:
#         return 0
#     if fn == 0:
#         return 1
#     f = list(set(f))
#     s = [0 for i in range(fn)]
#     while next_set(s, len(f)):
#         if arr_mask_mul(f, s) <= n:
#             ans += 1
#     return ans


# def mega_slow(n): # O(n log(n))
#     ans = 0
#     for i in range(1, n + 1):
#         if gcd(i, n) > 1:
#             ans += 1
#     return ans


def slow(n):  # O(n * fct(n))
    f = factor(n)
    ans = 0
    if n == 1 or n == 0:
        return 0
    if len(f) == 0:
        return 1
    for i in range(n):
        for j in f:
            if i % j == 0:
                ans += 1
                break
    return ans


def fast(n):  # O(sqrt(n))
    f = factor(n)
    fn = len(f)
    if n == 1 or n == 0:
        return 0
    if fn == 0:
        return 1
    remain = reseto(n, f)
    return n - remain - 1


def super_fast(n):  # O(sqrt(n))
    return n - euler_func(n)


n = int(input())
print(super_fast(n))

# for n in range(1000):
#     if (sfst := super_fast(n)) != (slw := slow(n)):
#         print(n, sfst, slw)

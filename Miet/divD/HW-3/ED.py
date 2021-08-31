
def fast_mod_pow(n, p, mod):
    if p == 0:
        return 1 % mod
    if p == 1:
        return n % mod
    if p % 2:
        return (n * fast_mod_pow(n, p - 1, mod)) % mod
    s = fast_mod_pow(n, p // 2, mod)
    return (s * s) % mod


x, y, p = input().split()
x, y, p = int(x), int(y), int(p)
print(fast_mod_pow(x, y, p))

# for p in range(990, 1000):
#     x = 990559
#     y = 994307
#     p = 999883
#     fst = fast_mod_pow(x, y, p)
#     slw = pow(x, y) % p
#     if fst != slw:
#         print()
#         print(x, y, p)
#     print('.', end='')

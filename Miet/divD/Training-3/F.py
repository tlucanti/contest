
def fast_mod_pow(n, p, mod):
    if p == 0:
        return 1 % mod
    if p == 1:
        return n % mod
    if p % 2:
        return (n * fast_mod_pow(n, p - 1, mod)) % mod
    s = fast_mod_pow(n, p // 2, mod)
    return (s * s) % mod


m1 = 1
m2 = 1

c = 10 * m1 + 4
n = 10 * m2 + 3

# c = 10 * m1 + 9
# n = 10 * m2 + 8


def g(k):
    return (fast_mod_pow(n, k, 10) + c) % 10


with open('input.txt', 'r') as f:
    t = int(f.readline())

with open('output.txt', 'w') as f:
    ans = g(t)
    f.write('{}\n'.format(ans))

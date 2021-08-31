def fast_mod_pow(n, p, mod):
    if p == 0:
        return 1 % mod
    if p == 1:
        return n % mod
    if p % 2:
        return (n * fast_mod_pow(n, p - 1, mod)) % mod
    s = fast_mod_pow(n, p // 2, mod)
    return (s * s) % mod


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


with open('input.txt') as inp:
    n, m = inp.readline().split()
    n, m = int(n), int(m)
    if n == 0 and m != 1:
        ans = 'ABSENT'
    else:
        ans = m

with open('output.txt', "w") as uot:
    uot.write('{}\n'.format(ans))

    # for i in range(1, n + 1):
    #     if fast_mod_pow(i, n, m) == 0:
    #         print(i)
    #         f = False
    #         break
    # if f:
    #     print('ABSENT')

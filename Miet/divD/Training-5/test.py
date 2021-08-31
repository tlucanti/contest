from random import randint as r


def hash_s(st, __pow_arr):
    ans = 0
    for __i in range(len(st)):
        ordc = ord(st[__i])
        ordc -= 65 if ordc < 96 else 71
        ans += ordc * __pow_arr[__i]
    ans += 52 * __pow_arr[len(st)]
    return ans


def hash_back(num):
    ans = []
    while num != 52:
        ordc = num % 52
        ordc += 65 if ordc < 26 else 71
        ans.append(ordc)
        num //= 52
    return ''.join(map(chr, ans))


def pow_arr_create(x, size):
    ans = [1 for __i in range(size)]
    for __i in range(1, size):
        ans[__i] = ans[__i - 1] * x
    return ans

j = 0
for i in range(150000 * 255):
    j += 1
print('ok')

pow_arr = pow_arr_create(52, 256)
for i in range(150000):
    n = r(255, 255)
    s = []
    for j in range(n):
        s.append(r(65, 90) + r(0, 1) * 32)
    s = ''.join(map(chr, s))
    s1 = hash_back(hash_s(s, pow_arr))
    if s != s1:
        print(s)
        print(hash_s(s, pow_arr))
        print(hash_back(hash_s(s, pow_arr)))
        print()


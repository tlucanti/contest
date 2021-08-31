def pow_arr_create(n, x):
    ar = [1]
    for _i in range(1, n):
        ar.append((ar[-1] * x) % 1000000007)
    return ar


def prefix_hash_create(s, x):
    h = [ord(s[0])]
    for _i in range(1, len(s)):
        h.append((h[-1] * x + ord(s[_i])) % 1000000007)
    return h


def hash_s(s, pow_arr):
    h = 0
    for i in range(len(s)):
        h += (ord(s[len(s) - i - 1]) * pow_arr[i]) % 1000000007
    return h % 1000000007


def issub(s1, s2, x):
    if len(s2) > len(s1):
        return 0
    if len(s2) == len(s1):
        return int(s1 == s2)
    h = hash_s(s2, pow_arr)
    pref = prefix_hash_create(s1, x)
    pref.append(0)
    for i in range(len(s1) - len(s2) + 1):
        h2 = (((pref[i + len(s2) - 1] - (pref[i - 1] * pow_arr[len(s2)])) % 1000000007) + 1000000007) % 1000000007
        if h == h2:
            return 1
    return 0


strs = []
x = 31
for t in range(int(input())):
    strs.append(input())
strs.sort(key=lambda i: len(i))
pow_arr = pow_arr_create(len(strs[-1]), x)
ans = 1
for i in range(1, len(strs)):
    if not issub(strs[i], strs[i - 1], x):
        ans = 0
        break
if ans == 0:
    print('NO')
else:
    print('YES')
    print('\n'.join(strs))

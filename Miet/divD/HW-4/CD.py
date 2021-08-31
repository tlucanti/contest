
def pow_arr_create(n, x):
    ar = [x]
    for _i in range(1, n):
        ar.append((ar[-1] * x) % 1000000007)
    return ar


def prefix_hash_create(s, pow_arr):
    h = [pow_arr[0] * ord(s[0])]
    for _i in range(1, len(s)):
        h.append((h[-1] + pow_arr[_i] * ord(s[_i])) % 1000000007)
    return h


def suffix_hash_create(s, pow_arr):
    l = len(s)
    h = [pow_arr[0] * ord(s[l - 1])]
    for _i in range(1, l):
        h.append((h[-1] + pow_arr[_i] * ord(s[l - _i - 1])) % 1000000007)
    return h


def solve(s1, s2, x):
    if len(s1) == 1:
        return [1]
    ans = []
    pow_arr = pow_arr_create(len(s1), x)
    pref1 = prefix_hash_create(s1, pow_arr)
    pref2 = prefix_hash_create(s2, pow_arr)
    suff1 = suffix_hash_create(s1, pow_arr)
    suff2 = suffix_hash_create(s2, pow_arr)
    if suff1[-2] == suff2[-1]:
        ans.append(1)
    for i in range(len(s2) - 1):
        if pref1[i] == pref2[i] and suff1[len(s2) - i - 2] == suff2[len(s2) - i - 2]:
            ans.append(i + 2)
    if pref1[len(s2) - 1] == pref2[len(s2) - 1]:
        ans.append(len(s2) + 1)
    return ans


# __input__ = open("input.txt", 'r')
# __output__ = open("output.txt", 'w')
# input = __input__.readline
# print = lambda *args: __output__.write(' '.join(map(str, args)) + '\n')

for i in range(1):
    x = 31
    s1 = input()
    s2 = input()
    ans = solve(s1, s2, x)
    print(len(ans))
    print(*ans)


# def solve_(s1, s2):
#     i1 = 0
#     i2 = 0
#     f = 1
#     while i1 < len(s1) and i2 < len(s2):
#         if s1[i1] != s2[i2]:
#             f = 0
#             break
#         sym1 = s1[i1]
#         sym2 = s2[i2]
#         c1 = 0
#         c2 = 0
#         while i1 < len(s1) and sym1 == s1[i1]:
#             i1 += 1
#             c1 += 1
#         while i2 < len(s2) and sym2 == s2[i2]:
#             i2 += 1
#             c2 += 1
#         if c1 > c2:
#             f = 0
#             break
#     if s1[-1] != s2[-1]:
#         f = 0
#     return f


def count(s):
    s = s.__iter__()
    ar = [[s.__next__(), 1]]
    for i in s:
        if i == ar[-1][0]:
            ar[-1][1] += 1
        else:
            ar.append([i, 1])
    return ar


def solve(s1, s2):
    ar1 = count(s1)
    ar2 = count(s2)
    if len(ar1) != len(ar2):
        return 0
    for i in range(len(ar1)):
        if ar1[i][0] != ar2[i][0] or ar1[i][1] > ar2[i][1]:
            return 0
    return 1


n = int(input())
for q_ in range(n):
    _s1 = input()
    _s2 = input()
    # print(count(_s1))
    # print(count(_s2))
    _f = solve(_s1, _s2)
    print("YES" if _f else "NO")

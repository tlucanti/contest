def fast_mod_pow(n, p, mod):
    if p < 0:
        return 1
    if p == 0:
        return 1 % mod
    if p == 1:
        return n % mod
    if p % 2:
        return (n * fast_mod_pow(n, p - 1, mod)) % mod
    s = fast_mod_pow(n, p // 2, mod)
    return (s * s) % mod


def fast_pow(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n
    if p % 2:
        return n * fast_pow(n, p - 1)
    s = fast_pow(n, p // 2)
    return s * s


def fp(dva_start, dva_end, tri_start, tri_end):
    tri_sum = (fast_pow(3, tri_end) - fast_pow(3, tri_start))
    dva_sum = (fast_pow(2, dva_end) - fast_pow(2, dva_start))
    sum = ((tri_sum * dva_sum) // 2) % 1000000007
    return sum


# def fmp(dva_start, dva_end, tri_start, tri_end):
#     tri_sum = (fast_mod_pow(3, tri_end, 1000000007) - fast_mod_pow(3, tri_start, 1000000007))
#     while tri_sum < 0:
#         tri_sum += 1000000007
#     if dva_start == 0:
#         tri_sum //= 2
#         dva_sum = fast_mod_pow(2, dva_end - 1, 1000000007)
#     else:
#         dva_sum = (fast_mod_pow(2, dva_end - 1, 1000000007) - fast_mod_pow(2, dva_start - 1, 1000000007))
#     while dva_sum < 0:
#         dva_sum += 1000000007
#     sum = (tri_sum * dva_sum) % 1000000007
#     return sum

def fmp(dva_start, dva_end, tri_start, tri_end):
    
    while tri_sum < 0:
        tri_sum += 1000000007
    # if dva_start == 0:
    #     tri_sum //= 2
    #     dva_sum = fast_mod_pow(2, dva_end - 1, 1000000007)
    # else:
    dva_sum = (fast_mod_pow(2, dva_end, 1000000007) - fast_mod_pow(2, dva_start, 1000000007))
    while dva_sum < 0:
        dva_sum += 1000000007
    sum = (tri_sum * dva_sum) % 1000000007
    return sum



# from random import randint as r
# m = 3
# for i in range(1000):
#     dva_start, dva_end, tri_start, tri_end = r(0, m), r(0, m), r(0, m), r(0, m) #input().split()
#     tri_start, tri_end = int(tri_start), int(tri_end) + 1
#     dva_start, dva_end = int(dva_start), int(dva_end) + 1
#     fpp = fp(dva_start, dva_end, tri_start, tri_end)
#     fmpp = fmp(dva_start, dva_end, tri_start, tri_end)
#     #print(fpp - fmpp, fpp, fmpp)
#     # print(fmpp)
#     if fpp - fmpp != 0:
#         print(fpp - fmpp, fpp, fmpp, '#', dva_start, dva_end, tri_start, tri_end)

for i in range(int(input())):
    dva_start, dva_end, tri_start, tri_end = input().split()
    tri_start, tri_end = int(tri_start), int(tri_end) + 1
    dva_start, dva_end = int(dva_start), int(dva_end) + 1
    fpp = fp(dva_start, dva_end, tri_start, tri_end)
    fmpp = fmp(dva_start, dva_end, tri_start, tri_end)
    print(fmpp, fpp)
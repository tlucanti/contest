
def inp():
    return list(map(int, input().split()))


n, d = inp()
a = inp()
i = 0
j = n - 1
ans = 0
a.sort()
# if n == 1:
#     if a[0] > d:
#         ans = 1
#     else:
#         ans = 0

while i <= j:
    power = a[j]
    if power > d:
        ans += 1
        j -= 1
        continue
    while i < j:
        power += a[j]
        i += 1
        if power > d:
            ans += 1
            j -= 1
            break
    if i >= j:
        break
print(ans)

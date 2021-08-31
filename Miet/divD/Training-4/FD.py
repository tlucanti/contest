n = int(input())
s = input()
keys = dict()
ans = 0
for i in range(n - 1):
    k = s[2 * i]
    r = s[2 * i + 1].lower()
    if k == r:
        continue
    keys[k] = keys.get(k, 0) + 1
    if keys.get(r, 0) > 0:
        keys[r] -= 1
    else:
        ans += 1
print(ans)


def g(n):
    a = n
    while n:
        a *= n % 10
        n //= 10
    return a

n = int(input())
ok = 0
ans = 0
for i in range(1, 10000):
    if g(i) == n and '1' not in str(i):
        ans = i
        ok += 1
if ok == 1:
    print(ans)
else:
    print('ERROR')


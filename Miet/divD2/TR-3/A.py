
def inp():
    return list(map(int, input().split()))

def prime(n):
    ans = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            ans.add(i)
            n //= i
        else:
            i += 1
    if n != 1:
        ans.add(n)
    return ans

x, n = inp()
p = prime(x)
print(p)
ans = 1
MOD = int(1e9) + 7
for i in p:
    a = i
    while a <= n:
        ans = ans * a # % MOD
        a = a * i

print(ans)


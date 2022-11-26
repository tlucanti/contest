
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
    return sorted(ans)

def modpow(a, n, MOD=int(1e9) + 7):
    if n == 0:
        return 1 % MOD
    elif n == 1:
        return a % MOD
    elif n % 2 == 1:
        return (a * modpow(a, n - 1, MOD)) % MOD
    aa = modpow(a, n // 2, MOD)
    return (aa * aa) % MOD

def powcnt(x, n):
    pw = n // x
    ans = 1
    while pw > 0:
        ans = (ans * modpow(x, pw)) % MOD
        pw //= x
    return ans

x, n = inp()
p = prime(x)
ans = 1
MOD = int(1e9) + 7
for pp in p:
    ans = (ans * powcnt(pp, n)) % MOD

print(ans)


##
#	Author:		antikostya
#	Created:	2021-11-28 17:20:23
#	Modified:	2021-11-28 19:20:57
##

def inp():
	return list(map(int, input().split()))

primes = set()

def isprime(n):
	if n == 1:
		return False
	if n in primes:
		return True
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	primes.add(n)
	return True


_t = int(input())
for _ in range(_t):
	n, e = inp()
	a = inp()
	ans = 0
	ar = [0] * n
	for i in range(n):
		if a[i] == 1:
			if i - e < 0 or a[i - e] != 1:
				ones = 0
				for o in range(i, n, e):
					if a[o] == 1:
						ones += 1
					else:
						break
				if i + e * ones < n and isprime(a[i + e * ones]):
					ans += ones
					ar[i + e * ones] = ones
				if i - e >= 0 and isprime(a[i - e]):
					ans += ones
					if ar[i - e] > 0:
						ans += ones * ar[i - e]

	print(ans)

##
#	Author:		antikostya
#	Created:	2021-10-17 14:01:39
#	Modified:	2021-10-17 14:38:18
##

def is_prime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True


for _t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	sm = sum(a)
	if is_prime(sm):
		for i in range(n):
			if not is_prime(sm - a[i]):
				r = list(range(1, n + 1))
				r.remove(i + 1)
				print(n - 1)
				print(*r)
				break
	else:
		print(n)
		print(*range(1, n + 1))

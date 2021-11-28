##
#	Author:		antikostya
#	Created:	2021-10-24 12:33:40
#	Modified:	2021-10-24 14:39:39
##

def gcd(a, b):
	def __gcd(a, b):
		# a > b
		if a % b == 0:
			return b
		return gcd(b, a % b)
	return __gcd(max(a, b), min(a, b))


for _ in range(int(input())):
	n = int(input())
	s = list(map(int, input().split()))
	ans = [0] * n
	if n % 2:
		to = n - 3
	else:
		to = n
	for i in range(0, to, 2):
		g = gcd(abs(s[i]), abs(s[i + 1]))
		ans[i] = -s[i + 1] // g
		ans[i + 1] = s[i] // g
	if n % 2:
		i1 = -3
		i2 = -2
		i3 = -1
		if s[i1] + s[i2] == 0:
			i1 = -3
			i2 = -1
			i3 = -2
		if s[i1] + s[i2] == 0:
			i1 = -2
			i2 = -1
			i3 = -3
		sm = s[i1] + s[i2]
		ans[i1] = -s[i3]
		ans[i2] = -s[i3]
		ans[i3] = sm
	print(*ans)

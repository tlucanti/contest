##
#	Author:		antikostya
#	Created:	2021-11-28 21:54:31
#	Modified:	2021-11-28 22:13:13
##

import math

def LCM(a, b):
	return a * b // math.gcd(a, b)

def divisors(n):
	ans = []
	for i in range(1, n + 1):
		if n % i == 0:
			ans.append(i)
	return ans
 
 
def check_div(s, n):
	div = a[:n]
	for i in range(len(s) // n):
		if s[n * i:n * (i + 1)] != div:
			return False
	return True
 

for i in range(int(input())): 
	a, b = input(), input()
	divs = divisors(len(a))
	ans = 0
	lcm = None
	for div in divs:
		if len(b) % div != 0:
			continue
		if not check_div(a, div):
			continue
		if not check_div(b, div):
			continue
		if a[:div] != b[:div]:
			continue
		if lcm is None:
			lcm = a[:div]
		elif len(lcm) > len(a[:div]):
			lcm = a[:div]

	if lcm is None:
		print(-1)
	else:
		print(lcm * LCM(len(a) // len(lcm), len(b) // len(lcm)))

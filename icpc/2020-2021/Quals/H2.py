##
#	Author:		antikostya
#	Created:	2021-12-19 12:33:45
#	Modified:	2021-12-19 15:59:38
##

import sys

def to_rim(n):
	U = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
	T = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
	H = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
	S = ['', 'M', 'MM', 'MMM']
	#
	ans = ''
	ans += S[(n % 10000) // 1000]
	ans += H[(n % 1000) // 100]
	ans += T[(n % 100) // 10]
	ans += U[n % 10]
	return ans


def is_pal(s):
	return s == s[::-1]


def startswith(s, i, b):
	return s[i:i + len(b)] == b


pals = ['I', 'II', 'III', 'V', 'X', 'XIX', 'XX', 'XXX', 'L', 'C', 'CXC', 'CC', 'CCC', 'D', 'M', 'MCM', 'MM', 'MMM']

def solve(n, s):
	i = 0
	ans = []
	while i < n:
		p = 0
		for pl in pals:
			if startswith(s, i, pl):
				p = max(p, len(pl))
		ans.append(s[i:i + p])
		i += p
	return ans

def solve_pal(n, s):
	if n % 2 == 0:
		left = s[:n // 2 - 1]
		sl1 = solve(len(left), left)
		sl2 = solve(len(left), left[::-1])
		if len(sl1) <= len(sl2):
			sl = sl1
		else:
			sl = sl2[::-1]
		return sl + [s[n // 2 - 1:n // 2 + 1]] + sl[::-1]
	else:
		left = s[:n // 2 - 1]
		sl = solve(len(left), left)
		return sl + [s[n // 2 - 1:n // 2 + 2]] + sl[::-1]

n = int(input())
s = input()
if n == 1:
	print(1)
	print(s)
	sys.exit(0)
if s == s[::-1]:
	a = solve_pal(n, s)
	print(len(a))
	print('\n'.join(a))
	sys.exit(0)
a1 = solve(n, s)
a2 = solve(n, s[::-1])
if len(a1) <= len(a2):
	print(len(a1))
	print('\n'.join(a1))
else:
	print(len(a2))
	print('\n'.join(a2[::-1]))



##
#	Author:		antikostya
#	Created:	2021-12-19 12:33:45
#	Modified:	2021-12-19 15:29:19
##

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
pals2 = ['XXXIX', 'MMMCM', 'CCCXC']
pals3 = ['XXIX', 'MMCM', 'CCXC']

def solve(n, s):
	ans = []
	i = 0
	while i < n - 2:
		p = s[i:i + 3]
		if p in ('XIX', 'CXC', 'MCM'):
			ans.append(p)
			i += 3
		else:
			ans.append(s[i])
			i += 1 
	if i == n - 2:
		ans.append(s[i])
		i += 1
	if i == n - 1:
		ans.append(s[i])
	i = 0
	s = ans
	ans = []
	while i < len(s) - 2:
		p = ''.join(s[i:i + 3])
		if p in ('III', 'XXX', 'CCC', 'MMM'):
			ans.append(p)
			i += 3
		else:
			ans.append(s[i])
			i += 1
	if i == len(s) - 2:
		ans.append(s[i])
		i += 1
	if i == len(s) - 1:
		ans.append(s[i])
	i = 0
	s = ans
	ans = []
	while i < len(s) - 2:
		p = ''.join(s[i:i + 2])
		if p in ('II', 'XX', 'CC', 'MM'):
			ans.append(p)
			i += 2
		else:
			ans.append(s[i])
			i += 1
	if i == len(s) - 2:
		ans.append(s[i])
		i += 1
	if i == len(s) - 1:
		ans.append(s[i])
	return ans


s = solve(int(input()), input())
print(len(s))
print('\n'.join(s))
exit(0)

A = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
import random

for i in range(1, 1000):
	if i % 1000 == 0:
		print(i)
	r = ''
	for a in A:
		r += random.randint(0, 100) * a
	r = list(r)
	random.shuffle(r)
	r = ''.join(r)
	an = solve(len(r), r)
	if ''.join(an) != r:
		print(r, an)

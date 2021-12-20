##
#	Author:		antikostya
#	Created:	2021-12-19 12:33:45
#	Modified:	2021-12-19 13:15:34
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
pals2 = ['XXXIX', 'CCCDC', 'MMMCM']

n = int(input())
s = input()
i = 0
ans = []
dp = [0] + [200000] * (n + 4)
for i in range(n):
	for pl in pals:
		if startswith(s, i, pl):
			dp[i + len(pl)] = min(dp[i] + 1, dp[i + len(pl)])
print(dp)


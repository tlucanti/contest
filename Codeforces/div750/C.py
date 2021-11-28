##
#	Author:		antikostya
#	Created:	2021-10-24 12:33:40
#	Modified:	2021-10-24 14:01:54
##

from string import ascii_lowercase as alp

for _ in range(int(input())):
	n = int(input())
	s = input()
	ANS = -1
	for a in alp:
		l = 0
		r = n - 1
		bool = True
		ans = 0
		while l < r:
			if s[l] == s[r]:
				l += 1
				r -= 1
			elif s[l] == a:
				ans += 1
				l += 1
			elif s[r] == a:
				ans += 1
				r -= 1
			else:
				bool = False
				break
		if bool:
			if ANS == -1:
				ANS = ans
			else:
				ANS = min(ANS, ans)
	print(ANS)

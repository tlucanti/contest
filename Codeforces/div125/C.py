# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-22 17:33:58
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-22 18:45:17

_It = int(input())
for _ in range(_It):
	n = int(input())
	s = input()
	c = 0
	i = 0
	while i < len(s) - 1:
		aa = s[i:i+2]
		if aa == '((' or aa == '))' or aa == '()':
			c += 1
			i += 2
		else:  # aa == ')('
			j = i
			i += 2
			while i < len(s) and s[i] != ')':
				i += 1
			if i < len(s):
				c += 1
				i += 1
			else:
				i = j
				break
	print(c, len(s) - i)


# pows = [0] * 6 * 100000
# p[0] = 1
# intmax = 2 ** 64
# for i in range(1, len(pows)):
# 	p[i] = (p[i - 1] * i) % intmax

# def hash_array(s):
# 	h = [0] * len(s)
# 	for i in range(len(s)):
# 		h[i] = (ord(s[i]) - ord('a') + 1) * pows[i]
# 		if i:
# 			h[i] += h[i - 1]


# def streq(s1, H1, i1, s2, H2, i2, size):
# 	h1 = H1[i1 + size - 1]
# 	if i1:
# 		h1 -= h[i1 - 1]
# 	h2 = H2[i2 + size - 1]
# 	if i2:
# 		h2 -= h[i2 - 1]

# 	if (i1 <= i2 and h1 * pows[i2 - i1] == h2) or \
# 		(i1 > i2 and h1 == h2 * pows[i1 - i2]):
# 		return True
# 	return False



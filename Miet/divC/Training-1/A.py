# -*- coding: utf-8 -*-
# @Author: kostya
# @Date:   2021-11-13 17:21:28
# @Last Modified by:   kostya
# @Last Modified time: 2021-11-14 00:44:00
 
def wrap(s):
	if s == '':
		return []
	ans = [[s[0], 1]]
	for i in range(1, len(s)):
		if s[i] == ans[-1][0]:
			ans[-1][1] += 1
		else:
			ans.append([s[i], 1])
	return ans
 
for _ in range(int(input())):
	s = input()
	if not ('1' in s and '2' in s and '3' in s):
		print(0)
		continue
	ans = len(s)
	wr = wrap(s)
	for i in range(1, len(wr) - 1):
		if ''.join(sorted(wr[i - 1][0] + wr[i][0] + wr[i + 1][0])) == '123':
			ans = min(ans, wr[i][1] + 2)
	print(ans)

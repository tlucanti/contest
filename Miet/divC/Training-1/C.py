# -*- coding: utf-8 -*-
# @Author: kostya
# @Date:   2021-11-13 23:34:45
# @Last Modified by:   kostya
# @Last Modified time: 2021-11-14 00:10:40

for _ in range(int(input())):
	d = dict()
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	srt = sorted(a)
	for i, p in enumerate(srt):
		d[p] = i
	s_i = d[a[0]]
	ans = 1
	for a_i in range(n):
		if s_i >= n or a[a_i] != srt[s_i]:
			ans += 1
			s_i = d[a[a_i]]
		s_i += 1
	if ans <= k:
		print('Yes')
	else:
		print('No')

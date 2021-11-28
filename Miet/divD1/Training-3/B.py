# -*- coding: utf-8 -*-
# @Author: kostya
# @Date:   2021-11-21 16:52:23
# @Last Modified by:   kostya
# @Last Modified time: 2021-11-21 17:46:02

import itertools

def lsd_radix_sort(arr):
	def get_digit(n, i):
		return n % ranks[i + 1] // ranks[i]
	dn = len(str(max(arr)))
	ranks = [1] * (dn + 1)
	for i in range(1, dn + 1):
		ranks[i] = ranks[i - 1] * 10
	for d in range(dn):
		bins = [[] for i in range(10)]
		for i in range(len(arr)):
			bins[get_digit(arr[i], d)].append(arr[i])
		arr = list(itertools.chain(*bins))
	return arr


n = int(input())
a = lsd_radix_sort(list(map(int, input().split())))

ans = 0
problems = 1
for i in range(n):
	if a[i] >= problems:
		ans += 1
		problems += 1

print(ans)

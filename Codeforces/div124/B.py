# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-10 17:26:31
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-10 18:04:04

for _ in range(int(input())):
	n = int(input())
	if n > 50 or 3 ** (n - 1) > 1_000_000_000:
		print('NO')
	else:
		print('YES')
		print(*[3 ** i for i in range(n)])

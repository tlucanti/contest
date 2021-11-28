# -*- coding: utf-8 -*-
# @Author: kostya
# @Date:   2021-11-13 17:02:53
# @Last Modified by:   kostya
# @Last Modified time: 2021-11-13 17:05:58

n, t = map(int, input().split())
s = input()
for i in range(t):
	s = s.replace('BG', 'GB')
print(s)

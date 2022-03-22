# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-10 17:26:31
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-11 12:44:12


def inp():
	return list(map(int, input().split()))


def arr_sub(arr, n):
	return [abs(i - n) for i in arr]


for _ in range(int(input())):
	n = int(input())
	a = inp()
	b = inp()
	left = abs(a[0] - b[0])
	left_up = min(arr_sub(b, a[0]))
	left_down = min(arr_sub(a, b[0]))

	right = abs(a[-1] - b[-1])
	right_up = min(arr_sub(b, a[-1]))
	right_down = min(arr_sub(a, b[-1]))

	diag_left_up = abs(a[0] - b[-1])
	diag_left_down = abs(a[-1] - b[0])

	m1 = min(left, left_up + left_down)
	m2 = min(right, right_up + right_down)
	m3 = min(diag_left_up, left_up + right_down)
	m4 = min(diag_left_down, left_down + right_up)

	print(min(m1 + m2, m3 + m4))

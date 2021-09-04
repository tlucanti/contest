##
#	Author:		kostya
#	Created:	2021-09-03 23:14:23
#	Modified:	2021-09-04 18:36:03
##

import random


VERBOSE = False


def solve(n, __s):
	s = __s.copy()
	crutch = int(3e9)
	for i in range(n):
		s[i] += crutch
	l_cumsum = [0] * n
	r_cumsum = [0] * n

	for i in range(1, n):
		l_cumsum[i] = l_cumsum[i - 1] + s[i - 1]
	for i in range(n - 2, -1, -1):
		r_cumsum[i] = r_cumsum[i + 1] + s[i + 1]

	dist = r_cumsum[0]
	ans = s[0]
	if VERBOSE:
		print(l_cumsum)
		print(r_cumsum)
	for i in range(n):
		right = r_cumsum[i] - s[i] * (n - i - 1)
		left = s[i] * i - l_cumsum[i]
		dst_tmp = left + right
		if VERBOSE:
			print(f'{i} >> r: {right}, l: {left}')
		if dst_tmp < dist:
			dist = dst_tmp
			ans = s[i]
	return ans - crutch


def slow(n, s):
	def distf(i):
		sm = 0
		for _i in s:
			sm += abs(_i - i)
		return sm

	dist = distf(0)
	ans = s[0]
	for i in range(s[0], s[-1] + 1):
		dst = distf(i)
		if dst < dist:
			dist = dst
			ans = i
	return ans


def test(t=100, nl=(10, 20), lim=(-100, 100)):
	for t in range(t):
		n = random.randint(*nl)
		inp = [0] * n
		for i in range(n):
			inp[i] = random.randint(*lim)
		inp.sort()
		a1 = solve(n, inp)
		a2 = slow(n, inp)
		if a1 != a2:
			print(inp)
			print(a1, a2)
			print()


def main():
	n = int(input())
	s = list(map(int, input().split()))
	print(solve(n, s))


# test(10000, (1, 4), (-10, 10))
main()

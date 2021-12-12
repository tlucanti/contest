##
#	Author:		antikostya
#	Created:	2021-12-12 17:57:48
#	Modified:	2021-12-12 20:04:51
##

def inp():
	return list(map(int, input().split()))

def wrap(lst, n, rev=False):
	a = []
	if rev:
		lst = lst[::-1]
	for i in range(0, len(lst), n):
		a.append(lst[i:i+n])
		if rev:
			a[-1] = a[-1][::-1]
	if rev:
		return a[::-1]
	return a

def count(lst):
	ans = 0
	for i in range(1, len(lst)):
		ans += abs(lst[i] - lst[i - 1])
	ans += abs(lst[0]) + abs(lst[-1])
	return ans

def solve(a, wrp):
	ans = 0
	for wr in wrp[::-1]:
		ans += count(wr)
	return ans - abs(a[0])

def hist(a):
	d = dict()
	for i in a:
		d[i] = d.get(i, 0) + 1
	return d

def gen(hi):
	ans = []
	for i in hi:
		ans += [i] * hi[i]
	return ans

_T = int(input())
for _t in range(_T):
	n, k = inp()
	a = inp()
	pos = [i for i in a if i > 0]
	neg = [i for i in a if i < 0]
	pos.sort()
	neg.sort()
	a = pos
	if len(a) == 0:
		p = 0
		pos = [0]
	else:
		p = min(
			solve(a, wrap(a, k, 0)),
			solve(a, wrap(a, k, 1)),
			solve(a[::-1], wrap(a[::-1], k, 0)),
			solve(a[::-1], wrap(a[::-1], k, 1)),
		)
	a = neg
	if len(a) == 0:
		n = 0
		neg = [0]
	else:
		n = min(
			solve(a, wrap(a, k, 0)),
			solve(a, wrap(a, k, 1)),
			solve(a[::-1], wrap(a[::-1], k, 0)),
			solve(a[::-1], wrap(a[::-1], k, 1)),
		)
	print(p + n + min(abs(pos[-1]), abs(neg[0])))

##
#	Author:		antikostya
#	Created:	2021-12-18 18:32:04
#	Modified:	2021-12-18 20:17:37
##

import itertools

def inp():
	return list(map(int, input().split()))

def wrap(s):
	f = lambda x: x
	g = itertools.groupby(s, f)
	ret = []

	for i in g:
		l = list(i)
		ret.append((l[0], len(list(l[1]))))
	return ret

def to_dec(num, base):
	ans = 0
	for i in range(len(num)):
		ans += num[i] * base[i]
	return ans

def pow_gen(base):
	base = base[::-1]
	ans = [1]
	for i in range(0, len(base)):
		ans.append(ans[-1] * base[i])
	return ans[::-1]

_T = int(input())
for _t in range(_T):
	n, k, x = inp()
	x -= 1
	s = input()
	if s.count('*') == 0 or x == 0:
		print(s.replace('*', ''))
		continue
	g = s.replace('a', ' ')
	g = [len(i) * k + 1 for i in g.split()]
	base = pow_gen(g)[1:]
	# print(g, base)
	num = [0] * len(base)
	num[0] = max(min(g[0], x // base[0] - 1), 0)
	i = 0
	dec = base[0] * num[0]
	while (1):
		num[i] += 1
		dec += base[i]
		if dec == x:
			break
		elif dec > x:
			dec -= base[i]
			num[i] -= 1
			i += 1
			num[i] = max(min(g[i], (x - dec) // base[i] - 1), 0)
			dec += num[i] * base[i]
		else:
			continue
	# print('ans:', num)
	a = wrap(s)
	j = 0
	for i in range(len(a)):
		if a[i][0] == '*':
			a[i] = num[j] * 'b'
			j += 1
		else:
			a[i] = 'a' * a[i][1]
	print(''.join(a))

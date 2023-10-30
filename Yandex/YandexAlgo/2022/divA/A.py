##
#	Author:		antikostya
#	Created:	2021-09-04 18:45:01
#	Modified:	2021-09-04 19:40:25
##

class Values(object):
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.zeronum = (a, b, c, d).count(0)

	def __call__(self, zeronum):
		return self.zeronum == zeronum


def solve(a, b, c, d):
	v = Values(a, b, c, d)
	if v(3):
		if c != 0:
			return 'INF'
		elif d != 0:
			return 'INF'
		else:
			raise RuntimeError('v(3)')
	elif c != 0 and v(2):
		if a != 0:
			return 'NO'
		elif b != 0:
			return 'NO'
		elif d != 0:
			return 'INF'
		else:
			raise RuntimeError('v(2)-c')
	elif d != 0 and v(2):
		if a != 0:
			return 0
		elif b != 0:
			return 'NO'
		else:
			raise RuntimeError('v(2)-d')
	elif v(1):
		if a == 0:
			return 'NO'
		elif b == 0:
			return 0
		elif c == 0:
			if b % a == 0:
				return -b // a
			else:
				return 'NO'
		elif d == 0:
			if b % a == 0:
				return -b // a
			else:
				return 'NO'
		else:
			raise RuntimeError('v(1)')
	elif v(0):
		if b % a == 0:
			x = -b // a
			if c * x + d == 0:
				return 'NO'
			else:
				return x
		else:
			return 'NO'
	else:
		raise RuntimeError('v')


def main():
	a, b, c, d = [int(input()) for i in range(4)]
	print(solve(a, b, c, d))


main()

from random import randint as r


class fraction(object):

	def __init__(self, numerator, denumerator):
		if denumerator == 0:
			raise ZeroDivisionError("denumenator cannot be zero")
		_gcd = self.gcd(numerator, denumerator)
		self.num = numerator // _gcd
		self.den = denumerator // _gcd

	@staticmethod
	def gcd(a, b):    # greatest common divisor
		def gcd_req(_a, _b):
			if _b == 0:
				return _a
			return gcd_req(_b, _a % _b)

		return gcd_req(max(a, b), min(a, b))

	@staticmethod
	def lcm(self, a, b):    # least common multiple
		if a * b == 0:
			return 0
		return abs(a * b) // self.gcd(a, b)

	def __add__(self, other):
		if isinstance(other, int):
			return fraction(other, 1) + self
		return fraction(self.num * other.den + other.num * self.den, self.den * other.den)

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		if isinstance(other, int):
			return self - fraction(other, 1)
		return fraction(self.num * other.den - other.num * self.den, self.den * other.den)

	def __rsub__(self, other):
		return self - other

	def __iadd__(self, other):
		self.num = self.num * other.den + other.num * self.den
		self.den = self.den * other.den
		_gcd = self.gcd(self.num, self.den)
		self.num //= _gcd
		self.den //= _gcd
		return self

	def __isub__(self, other):
		self.num = self.num * other.den - other.num * self.den
		self.den = self.den * other.den
		_gcd = self.gcd(self.num, self.den)
		self.num //= _gcd
		self.den //= _gcd

	def __eq__(self, other):
		return self.num == other.num and self.den == other.den

	def __ne__(self, other):
		return not self == other

	def __gt__(self, other):
		return self.num * other.den > other.num * self.den

	def __repr__(self):
		return f"{self.num}/{self.den}"

	def __str__(self):
		return f"{self.num}/{self.den}"


for i in range(200000):
	d = pow(2, r(1, 2))
	n = r(0, d)

	delay = fraction(n, d)
	ans = []
	bt = bin(delay.num)[2:][::-1]
	for j in range(len(bt)):
		if int(bt[j]):
			ans.append(fraction(pow(2, j), delay.den))
	if str(sum(ans) - delay) != '0/1':
		print()
		print(delay, end='')
	# else:
	# 	print('.', end='')
	# print('{:>10} {:>10} {:>10}'.format(str(sum(ans) - delay), str(sum(ans)), str(delay)))
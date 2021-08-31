
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

	def __sub__(self, other):
		return fraction(self.num * other.den - other.num * self.den, self.den * other.den)

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


duration = fraction(*map(int, input().split('/')))
for t in range(int(input())):
	s = input().split()
	n = int(s[0])
	cycle_sum = fraction(0, 1)
	for i in range(1, n + 1):
		cycle_sum += fraction(*map(int, s[i].split('/')))
	delay = duration - cycle_sum
	bt = bin(delay.num)[2:][::-1]
	print(bt.count('1'), end=' ')
	ans = []
	for j in range(len(bt)):
		if int(bt[j]):
			ans.append(fraction(pow(2, j), delay.den))
	print(*ans[::-1])
	# print(cycle_sum, delay)


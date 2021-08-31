
class fraction(object):

	def __init__(self, numerator, denumerator):
		if denumerator == 0:
			raise ZeroDivisionError("denumenator cannot be zero")
		_gcd = self.gcd(self, numerator, denumerator)
		self.num = numerator // _gcd
		self.den = denumerator // _gcd
		self.real_num = numerator
		self.real_den = denumerator

	@staticmethod
	def gcd(self, a, b):    # greatest common divisor
		def gcd_req(_a, _b):
			if _b == 0:
				return _a
			return gcd_req(_b, _a % _b)

		return gcd_req(max(a, b), min(a, b))

	@staticmethod
	def lcm(self, a, b):    # least common multiple
		if a * b == 0:
			return 0
		return abs(a * b) / self.gcd(a, b)

	def __eq__(self, other):
		return self.num == other.num and self.den == other.den

	def __ne__(self, other):
		return not self == other

	def __gt__(self, other):
		if self == other:
			return self.real_num > self.real_den
		return self.num * other.den > other.num * self.den

	def __repr__(self):
		return f"{self.num}/{self.den}"

	def __str__(self):
		return f"{self.num}/{self.den}"


class elem(object):

	def __init__(self, time, score, frac, num, avaliable):
		self.time = time
		self.score = score
		self.frac = frac
		self.num = num
		self.avaliable = avaliable

	def __repr__(self):
		return '{' + f"time: {self.time}, score: {self.score}, frac: {self.frac}, num: {self.num}, av: {self.avaliable}" + '}'


n = int(input())
arr = [None for _ in range(n)]
score = 0
item_ptr = n - 1
for i in range(n):
	t, c = map(int, input().split())
	arr[i] = elem(t, c, fraction(t, c), i, 1)
arr_frac = sorted(arr, key=lambda x: x.frac)[::-1]
# arr_score = sorted(arr, key=lambda x: x.score)[::-1]
for item in arr_frac:
	if not item.avaliable:
		break
	item.avaliable = 0
	score += item.score
	for t in range(item.time):
		if not arr_frac[item_ptr].avaliable:
			break
		arr_frac[item_ptr].avaliable = 0
		item_ptr -= 1
print(score)

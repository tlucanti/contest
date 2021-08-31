import math


class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __del__(self):
		del self.x
		del self.y

	def __repr__(self):
		# return '<point object at {}>'.format(hex(id(self)))
		return self.__str__()

	def __str__(self):
		return '({}, {})'.format(str(self.x), str(self.y))

	def __bytes__(self):
		return bytes((self.x, self.y))

	def __copy__(self):
		return point(self.x, self.y)

	def __hash__(self):
		return hash(self.__str__())

	def __len__(self):
		return pow(self.x * self.x + self.y * self.y, 0.5)

	def __getitem__(self, item):
		if item == 0 or item == -2:
			return self.x
		elif item == 1 or item == -1:
			return self.y
		else:
			raise IndexError('point has only two elements')

	def __setitem__(self, key, value):
		if key == 0 or key == -2:
			self.x = value
		elif key == 1 or key == -1:
			self.y = value
		else:
			raise IndexError('point has only two elements')

	def __reversed__(self):
		return point(self.y, self.x)

	def __contains__(self, item):
		return self.x == item or self.y == item

	def __bool__(self):
		return self.x != 0 and self.y != 0

	def __cmp__(self, other):
		return self.x * self.x + self.y * self.y - other.x * other.x + other.y * other.y

	def __lt__(self, other):
		return self.__abs__() < other.__abs__()

	def __le__(self, other):
		return self.__abs__() <= other.__abs__()

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return self.x != other.x or self.y != other.y

	def __gt__(self, other):
		return self.__abs__() > other.__abs__()

	def __ge__(self, other):
		return self.__abs__() >= other.__abs__()

	def __pos__(self):
		return self

	def __neg__(self):
		return point(-self.x, -self.y)

	def __abs__(self):
		return self.x * self.x + self.y * self.y

	def __invert__(self):
		return point(self.x, -self.y)

	def __round__(self, n=None):
		return point(round(self.x, n), round(self.y, n))

	def __floor__(self):
		return point(math.floor(self.x), math.floor(self.y))

	def __ceil__(self):
		return point(math.ceil(self.x), math.ceil(self.y))

	def __trunc__(self):
		return point(math.trunc(self.x), math.trunc(self.y))

	def __add__(self, other):
		return point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return point(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return point(self.x * other.x, self.y * other.y)

	def __floordiv__(self, other):
		return point(self.x // other.x, self.y // other.y)

	def __truediv__(self, other):
		return point(self.x / other.x, self.y / other.y)

	def __mod__(self, other):
		return point(self.x % other.x, self.y % other.y)

	def __divmod__(self, other):
		return self.__floordiv__(other), self.__mod__(other)

	def __pow__(self, power, modulo=None):
		return point(pow(self.x, power, modulo), pow(self.y, power, modulo))

	def __lshift__(self, other):
		if other % 2:
			return self.__reversed__()
		else:
			return self

	def __rshift__(self, other):
		if other % 2:
			return self.__reversed__()
		else:
			return self

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y

	def __imul__(self, other):
		self.x *= other.x
		self.y *= other.y

	def __ifloordiv__(self, other):
		self.x //= other.x
		self.y //= other.y

	def __idiv__(self, other):
		self.x /= other.x
		self.y /= other.y

	def __itruediv__(self, other):
		self.x /= other.x
		self.y /= other.y

	def __imod__(self, other):
		self.x %= other.x
		self.y %= other.y

	def __ipow__(self, other):
		self.x = pow(self.x, other)
		self.y = pow(self.y, other)

	def __complex__(self):
		return complex(self.x, self.y)

	def __matmul__(self, other):
		return self.x * other.y - self.y * other.x


def inside(p1, p2, p):
	return min(p1.x, p2.x) <= p.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= p.y <= max(p1.y, p2.y)


def solve(l1, r1, l2, r2):
	if l1 == l2 or l1 == r2 or r1 == l2 or r1 == r2:
		return True
	c1 = ((l2 - l1) @ (r1 - l1)) * ((r2 - l1) @ (r1 - l1))
	c2 = ((l1 - l2) @ (r2 - l2)) * ((r1 - l2) @ (r2 - l2))
	if c1 == c2 == 0:
		return inside(l1, r1, l2) or inside(l1, r1, r2) or inside(l2, r2, l1) or inside(l2, r2, r1)
	return c1 <= 0 and c2 <= 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
l1 = point(x1, y1)
r1 = point(x2, y2)
l2 = point(x3, y3)
r2 = point(x4, y4)

print('yes' if solve(l1, r1, l2, r2) else 'no')

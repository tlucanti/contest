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
		if isinstance(other, list) or isinstance(other, tuple):
			other = point(other[0], other[1])
		return self.__abs__() < other.__abs__()

	def __le__(self, other):
		if isinstance(other, list) or isinstance(other, tuple):
			other = point(other[0], other[1])
		return self.__abs__() <= other.__abs__()

	def __eq__(self, other):
		if isinstance(other, point):
			return self.x == other.x and self.y == other.y
		elif isinstance(other, list) or isinstance(other, tuple):
			return self.x == other[0] and self.y == other[1]

	def __ne__(self, other):
		if isinstance(other, point):
			return self.x != other.x or self.y != other.y
		elif isinstance(other, list) or isinstance(other, tuple):
			return self.x != other[0] or self.y != other[1]

	def __gt__(self, other):
		if isinstance(other, list) or isinstance(other, tuple):
			other = point(other[0], other[1])
		return self.__abs__() > other.__abs__()

	def __ge__(self, other):
		if isinstance(other, list) or isinstance(other, tuple):
			other = point(other[0], other[1])
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
		if isinstance(other, int):
			return point(self.x + other, self.y + other)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x + other[0], self.y + other[1])
		return point(self.x + other.x, self.y + other.y)

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		if isinstance(other, int):
			return point(self.x - other, self.y - other)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x - other[0], self.y - other[1])
		return point(self.x - other.x, self.y - other.y)
	
	def __rsub__(self, other):
		return self.__sub__(other)

	def __mul__(self, other):
		if isinstance(other, int):
			return point(self.x * other, self.y * other)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x * other[0], self.y * other[1])
		return point(self.x * other.x, self.y * other.y)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __floordiv__(self, other):
		if isinstance(other, int):
			return point(self.x // other, self.y // other)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x // other[0], self.y // other[1])
		return point(self.x // other.x, self.y // other.y)

	def __rfloordiv__(self, other):
		return self.__floordiv__(other)

	def __truediv__(self, other):
		if isinstance(other, int):
			return point(self.x / other, self.y / other)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x / other[0], self.y / other[1])
		return point(self.x / other.x, self.y / other.y)

	def __rtruediv__(self, other):
		return self.__truediv__(other)

	def __mod__(self, other):
		if isinstance(other, int):
			return point(self.x % other, self.y % other)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x % other[0], self.y % other[1])
		return point(self.x % other.x, self.y % other.y)

	def __rmod__(self, other):
		return self.__mod__(other)

	def __divmod__(self, other):
		return self.__floordiv__(other), self.__mod__(other)

	def __rdivmod__(self, other):
		return self.__divmod__(other)

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
		if isinstance(other, int):
			self.x += other
			self.y += other
		elif isinstance(other, list) or isinstance(other, tuple):
			self.x += other[0]
			self.y += other[1]
		self.x += other.x
		self.y += other.y

	def __isub__(self, other):
		if isinstance(other, int):
			self.x -= other
			self.y -= other
		elif isinstance(other, list) or isinstance(other, tuple):
			self.x -= other[0]
			self.y -= other[1]
		self.x -= other.x
		self.y -= other.y

	def __imul__(self, other):
		if isinstance(other, int):
			self.x *= other
			self.y *= other
		elif isinstance(other, list) or isinstance(other, tuple):
			self.x *= other[0]
			self.y *= other[1]
		self.x *= other.x
		self.y *= other.y

	def __ifloordiv__(self, other):
		if isinstance(other, int):
			self.x //= other
			self.y //= other
		elif isinstance(other, list) or isinstance(other, tuple):
			self.x //= other[0]
			self.y //= other[1]
		self.x //= other.x
		self.y //= other.y

	def __idiv__(self, other):
		if isinstance(other, int):
			self.x /= other
			self.y /= other
		elif isinstance(other, list) or isinstance(other, tuple):
			self.x /= other[0]
			self.y /= other[1]
		self.x /= other.x
		self.y /= other.y

	def __itruediv__(self, other):
		if isinstance(other, int):
			self.x /= other
			self.y /= other
		elif isinstance(other, list) or isinstance(other, tuple):
			self.x /= other[0]
			self.y /= other[1]
		self.x /= other.x
		self.y /= other.y

	def __imod__(self, other):
		if isinstance(other, int):
			self.x %= other
			self.y %= other
		elif isinstance(other, list) or isinstance(other, tuple):
			self.x %= other[0]
			self.y %= other[1]
		self.x %= other.x
		self.y %= other.y

	def __ipow__(self, other):
		self.x = pow(self.x, other)
		self.y = pow(self.y, other)

	def __complex__(self):
		return complex(self.x, self.y)

	def __matmul__(self, other):
		return self.x * other.y - self.y * other.x

	def __rmatmul__(self, other):
		return self.__matmul__(other)

	def __call__(self, *args, **kwargs):
		if args[0] == 'x':
			return point(self.x, 0)
		elif args[0] == 'y':
			return point(0, self.y)


def inside(p1, p2, p):
	return min(p1.x, p2.x) <= p.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= p.y <= max(p1.y, p2.y)


def true_inside(p1, p2, p):
	return min(p1.x, p2.x) < p.x < max(p1.x, p2.x) and min(p1.y, p2.y) < p.y < max(p1.y, p2.y)


def intersect(l1, r1, l2, r2):
	if l1 == l2 or l1 == r2 or r1 == l2 or r1 == r2:
		return True
	c1 = ((l2 - l1) @ (r1 - l1)) * ((r2 - l1) @ (r1 - l1))
	c2 = ((l1 - l2) @ (r2 - l2)) * ((r1 - l2) @ (r2 - l2))
	if c1 == c2 == 0:
		return inside(l1, r1, l2) or inside(l1, r1, r2) or inside(l2, r2, l1) or inside(l2, r2, r1)
	return c1 <= 0 and c2 <= 0


def true_intersect(l1, r1, l2, r2):
	if l1 == l2 or l1 == r2 or r1 == l2 or r1 == r2:
		return False
	c1 = ((l2 - l1) @ (r1 - l1)) * ((r2 - l1) @ (r1 - l1))
	c2 = ((l1 - l2) @ (r2 - l2)) * ((r1 - l2) @ (r2 - l2))
	return c1 < 0 and c2 < 0


def solve(a1, a2, b1, b2):
	d1 = b1 - a1
	d2 = b2 - a2
	if 0 in d1 or 0 in d2:
		return 0
	elif inside(a1, b1, a2) and inside(a1, b1, b2):
		p = b2 - a2
		return abs(p.x * p.y)
	elif inside(a2, b2, a1) and inside(a2, b2, b1):
		p = b1 - a1
		return abs(p.x * p.y)
	points = [a1, a2, b1, b2]
	x4c = sum(points)
	lines = (
		(a1, a1('x') + b1('y')),
		(a1, a1('y') + b1('x')),
		(b1, a1('x') + b1('y')),
		(b1, a1('y') + b1('x')),
		(a2, a2('x') + b2('y')),
		(a2, a2('y') + b2('x')),
		(b2, a2('x') + b2('y')),
		(b2, a2('y') + b2('x')),
	)
	for ln1 in range(len(lines)):
		for ln2 in range(ln1 + 1):
			if true_intersect(lines[ln1][0], lines[ln1][1], lines[ln2][0], lines[ln2][1]):
				x = sorted((lines[ln1][0].x, lines[ln1][1].x, lines[ln2][0].x, lines[ln2][1].x))[2]
				y = sorted((lines[ln1][0].y, lines[ln1][1].y, lines[ln2][0].y, lines[ln2][1].y))[2]
				points.append(point(x, y))
	if len(points) > 4:
		points += (a1('x') + b1('y'), a1('y') + b1('x'), a2('x') + b2('y'), a2('y') + b2('x'))
		points = list(set(points))
		points.sort(key=lambda x: abs(4 * x - x4c)) ! #CHECK ALL this points inside both squares
		p1 = points[0]
		p2 = None
		for i in points:
			if i.x != p1.x and i.y != p1.y and (inside(a1, b1, i) or inside(a2, b2, i)):
				p2 = i
				break
		if p2 is None:
			return 0
		p = p1 - p2
		return abs(p.x * p.y)
	else:
		return 0


x1, y1, x2, y2 = map(int, input().split())
a1, b1 = point(x1, y1), point(x2, y2)
x1, y1, x2, y2 = map(int, input().split())
a2, b2 = point(x1, y1), point(x2, y2)

print(solve(a1, a2, b1, b2))

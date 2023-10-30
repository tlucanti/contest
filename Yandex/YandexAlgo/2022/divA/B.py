##
#	Author:		kostya
#	Created:	2021-09-04 19:59:36
#	Modified:	2021-09-04 23:19:39
##

import math
import builtins


class point(object):
	"""
	class to present 2D point

	attributes
	----------
	x : object
		first coordinate
	y : object
		second coordinate

	methods
	-------

	__init__(x, y):
		call : point(x, y):
		class constructor

	Examples
	--------

	 Methods defined here:

	__del__(x, y):
		del self
		delete coordinates objects and the object itself


	"""
	def __init__(self, x, y):
		"""
		class constructor

		Parameters
		----------
		x : int, float
			first coordinate
		y : int, float
			second coordinate
		"""

		self.x = x
		self.y = y

	def __del__(self):
		del self.x
		del self.y
		del self

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
		return math.sqrt(self.x * self.x + self.y * self.y)

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
		if isinstance(other, list) or isinstance(other, tuple):
			other = point(other[0], other[1])
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
		if isinstance(other, int) or isinstance(other, float):
			return point(self.x + other, self.y + other)
		elif isinstance(other, complex):
			return point(self.x + other.real, self.y + other.imag)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x + other[0], self.y + other[1])
		return point(self.x + other.x, self.y + other.y)

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return point(self.x - other, self.y - other)
		elif isinstance(other, complex):
			return point(self.x - other.real, self.y - other.imag)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x - other[0], self.y - other[1])
		return point(self.x - other.x, self.y - other.y)

	def __rsub__(self, other):
		return self.__sub__(other)

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return point(self.x * other, self.y * other)
		elif isinstance(other, complex):
			return point(self.x * other.real, self.y * other.imag)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x * other[0], self.y * other[1])
		return point(self.x * other.x, self.y * other.y)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __floordiv__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return point(self.x // other, self.y // other)
		elif isinstance(other, complex):
			return point(self.x // other.real, self.y // other.imag)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x // other[0], self.y // other[1])
		return point(self.x // other.x, self.y // other.y)

	def __rfloordiv__(self, other):
		return self.__floordiv__(other)

	def __truediv__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return point(self.x / other, self.y / other)
		elif isinstance(other, complex):
			return point(self.x / other.real, self.y / other.imag)
		elif isinstance(other, list) or isinstance(other, tuple):
			other = point(self.x / other[0], self.y / other[1])
		return point(self.x / other.x, self.y / other.y)

	def __rtruediv__(self, other):
		return self.__truediv__(other)

	def __mod__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return point(self.x % other, self.y % other)
		elif isinstance(other, complex):
			return point(self.x % other.real, self.y % other.imag)
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
		return pow(self.x, power, modulo) + pow(self.y, power, modulo)

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
		return self + other

	def __isub__(self, other):
		return self - other

	def __imul__(self, other):
		return self * other

	def __ifloordiv__(self, other):
		return self // other

	def __idiv__(self, other):
		return self / other

	def __itruediv__(self, other):
		return self / other

	def __imod__(self, other):
		return self % other

	def __ipow__(self, other):
		self.x = pow(self.x, other)
		self.y = pow(self.y, other)
 
	def __complex__(self):
		return complex(self.x, self.y)
 
	def __matmul__(self, other):
		return self.x * other.y - self.y * other.x

	def norm(self):
		ln = len(self)
		self.x /= ln
		self.y /= ln

	def diag(self):
		return self.__abs__()


def len(__n):
	if isinstance(__n, point) or isinstance(__n, line):
		return __n.__len__()
	else:
		return builtins.len(__n)


class line(object):

	def __init__(self, p1, p2):
		self.a = p1
		self.b = p2
		self.d = p2 - p1
		self.abs = self.d.__abs__()
	
	def __abs__(self):
		return self.abs

	def __len__(self):
		return math.sqrt(self.abs)

	def __pow__(self, power, modulo=None):
		return self.d.__pow__(power, modulo)

	def intersect(self, other):
		def inside(p1, p2, p):
			return min(p1.x, p2.x) <= p.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= p.y <= max(p1.y, p2.y)
		
		l1, r1 = self.a, self.b
		l2, r2 = other.a, other.b
		if l1 == l2 or l1 == r2 or r1 == l2 or r1 == r2:
			return True
		c1 = ((l2 - l1) @ (r1 - l1)) * ((r2 - l1) @ (r1 - l1))
		c2 = ((l1 - l2) @ (r2 - l2)) * ((r1 - l2) @ (r2 - l2))
		if c1 == c2 == 0:
			return inside(l1, r1, l2) or inside(l1, r1, r2) or inside(l2, r2, l1) or inside(l2, r2, r1)
		return c1 <= 0 and c2 <= 0


class triangle(object):

	def __init__(self, p1, p2, p3):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3

	@staticmethod
	def triple_product(p1, p2, p3):
		return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

	def __contains__(self, other):
		"""
		0 - outside
		1 - on side
		2 - inside
		"""
		d1 = triple_product(other, self.p1, self.p2);
		d2 = triple_product(other, self.p2, self.p3);
		d3 = triple_product(other, self.p3, self.p1);
		

def solve(a, b, c, d):
	def __solve(a, b, c, d):
		ac = line(a, c)
		bd = line(b, d)
		ab = line(a, b)
		bc = line(b, c)
		cd = line(c, d)
		da = line(d, a)
		# print(ac**2 + bd**2, ab**2 + bc**2 + cd**2 + da**2)
		if ac**2 + bd**2 == ab**2 + bc**2 + cd**2 + da**2:
			return True
		else:
			return False

	if a == b or a == c or a == d or b == c or b == d or c == d:
		return 'NO'
	if line(a, c).intersect(line(b, d)):
		ans = __solve(a, b, c, d)
	else:
		ans = __solve(a, b, c, d)
	return 'YES' if ans else 'NO'


def main():
	n = int(input())
	for i in range(n):
		st = list(map(int, input().split()))
		a, b = point(st[0], st[1]), point(st[2], st[3])
		c, d = point(st[4], st[5]), point(st[6], st[7])			
		print(solve(a, b, c, d))


main()

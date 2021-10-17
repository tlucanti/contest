##
#	Author:		antikostya
#	Created:	2021-10-03 19:32:28
#	Modified:	2021-10-03 21:33:50
##

class Tile(object):
	def __init__(self, line1, line2):
		self.a = line1 + line2[::-1]

	def rotate(self):
		self.a = self.a[1:] + self.a[0]
		return self

	def __eq__(self, other):
		return self.a == other.a

	def __hash__(self):
		return hash(self.a)


tiles = dict()
n = int(input())
for i in range(n):
	new = Tile(input(), input())
	tiles[new] = tiles.get(new, 0) + 1
n, m = map(int, input().split())
MAP = [input() for i in range(n)]
for y in range(n // 2):
	for x in range(m // 2):
		ok = False
		carpet = Tile(MAP[y * 2][x * 2: (x+1) * 2], MAP[y * 2 + 1][x * 2: (x+1) * 2])
		for i in range(4):
			if tiles.get(carpet, 0) > 0:
				tiles[carpet] -= 1
				ok = True
				break
			carpet.rotate()
		if not ok:
			print('No')
			exit(0)
print('Yes')

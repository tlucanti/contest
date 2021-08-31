def inside(x1, x2, a):
	x1, x2 = min(x1, x2), max(x1, x2)
	if x1 < a < x2:
		return True
	return False


for i in range(int(input())):
	input()
	ax, ay = map(int, input().split())
	bx, by = map(int, input().split())
	fx, fy = map(int, input().split())

	if (ax == bx == fx and inside(ay, by, fy)) or (ay == by == fy and inside(ax, bx, fx)):
		print(abs(ax - bx) + abs(ay - by) + 2)
	else:
		print(abs(ax - bx) + abs(ay - by))

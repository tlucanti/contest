
def getc(s):
	d = list(map(int, s.split()))
	if d[0] == 0:
		c = [d[2] * 10, d[3] * 10]
	else:
		c = [5 * (d[1] + d[3] + d[5] + d[7]) // 2, 5 * (d[2] + d[4] + d[6] + d[8]) // 2]
	return c

n = int(input())
if n <= 2:
	for i in range(n):
		input()
	print("Yes")
else:
	c1 = getc(input())
	c2 = getc(input())
	upd = 0
	if c1 == c2:
		upd = 1
	checkdot = lambda c: ((c1[1] - c2[1]) * c[0] + (c2[0] - c1[0]) * c[1] + c1[0]*c2[1] - c2[0]*c1[1])
	f = 0

	for i in range(n - 2):
		c = getc(input())
		if upd:
			if c1 != c:
				c2 = c[:]
				checkdot = lambda c: ((c1[1] - c2[1]) * c[0] + (c2[0] - c1[0]) * c[1] + c1[0]*c2[1] - c2[0]*c1[1])
				upd = 0
		else:
			f = checkdot(c)
	print('Yes' if f==0 else 'No')
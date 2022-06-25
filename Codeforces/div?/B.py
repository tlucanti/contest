
for t in range(int(input())):
	n = int(input())
	ss = []
	a = []
	one_line = 0
	for i in range(n):
		ss.append(input())
	for i in range(n):
		for j in range(n):
			if ss[i][j] == '*':
				a.append((i, j))
	if a[0][0] == a[1][0]:
		if a[0][0] == 0:
			a.append((1, a[0][1]))
			a.append((1, a[1][1]))
		else:
			a.append((a[0][0] - 1, a[0][1]))
			a.append((a[1][0] - 1, a[1][1]))
	elif a[0][1] == a[1][1]:
		if a[0][1] == 0:
			a.append((a[0][0], 1))
			a.append((a[1][0], 1))
		else:
			a.append((a[0][0], a[0][1] - 1))
			a.append((a[1][0], a[1][1] - 1))
	else:
		a.append((a[0][0], a[1][1]))
		a.append((a[1][0], a[0][1]))
	for i in range(n):
		for j in range(n):
			if (i, j) in a:
				print('*', end='')
			else:
				print('.', end='')
		print()
	# print()

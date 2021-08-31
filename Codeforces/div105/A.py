
for t in range(int(input())):
	n, *urdl = map(int, input().split())
	if max(urdl) > n:
		print('NO')
		continue
	for i in range(4):
		typ = [None, None]
		if urdl[i] > n - 2:
			if urdl[i] - n + 2 == 1:
				typ[1] = 'b'
			else:
				typ = ['b', 'b']
		if urdl[i] < 2:
			if urdl[i] == 1:
				typ[0] = 'w'
			else:
				typ = ['w', 'w']
		urdl[i] = typ
	f = 0
	for i in range(16):
		rev = bin(i)[2:]
		rev = '0' * (4 - len(rev)) + rev
		urdl_cpy = urdl.copy()
		for j in range(4):
			if rev[j] == '1':
				urdl_cpy[j] = list(reversed(urdl_cpy[j]))
		flags = [0, 0, 0, 0]
		for j in range(4):
			f1 = 0
			f2 = 0
			if urdl_cpy[j][0] is None or urdl_cpy[j - 1][1] is None:
				f1 = 1
			elif urdl_cpy[j][0] == urdl_cpy[j - 1][1]:
				f1 = 1
			if urdl_cpy[j][1] is None or urdl_cpy[(j + 1) % 4][0] is None:
				f2 = 1
			elif urdl_cpy[j][1] == urdl_cpy[(j + 1) % 4][0]:
				f2 = 1
			if f1 and f2:
				flags[j] = 1
		if sum(flags) == 4:
			break
	if sum(flags) == 4:
		print('YES')
	else:
		print('NO')

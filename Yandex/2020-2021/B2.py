
def pr(d):
	for _i in range(len(d)):
		_s = ''.join(d[_i])
		print(_s[:3] + '_' + _s[3:])
		for _j in range(6):
			if d[_i][_j] == 'X':
				d[_i][_j] = '#'


n = int(input())
d = []
for i in range(n):
	d.append(list(''.join(input().split('_'))))
m = int(input())
abc = 'ABCDEF'
for __m in range(m):
	cnt, side, where = input().split()
	cnt = int(cnt)
	side = 0 if side == 'left' else 1
	where = 0 if where == 'window' else 2
	success = False
	for i in range(n):
		if success:
			break
		if cnt == 3:
			if side == 0:
				if d[i][:3] == list('...'):
					d[i][:3] = list('XXX')
					print(f'Passengers can take seats: {i + 1}A {i + 1}B {i + 1}C')
					success = True
			else:
				if d[i][3:] == list('...'):
					d[i][3:] = list('XXX')
					print(f'Passengers can take seats: {i + 1}D {i + 1}E {i + 1}F')
					success = True
		elif cnt == 2:
			if side == 0:
				if d[i][where] == '.' and d[i][1] == '.':
					d[i][where] = 'X'
					d[i][1] = 'X'
					p = ' '.join(sorted([f'{i + 1}{abc[where]}', f'{i + 1}B']))
					print(f'Passengers can take seats: {p}')
					success = True
			else:
				if d[i][5 - where] == '.' and d[i][4] == '.':
					d[i][5 - where] = 'X'
					d[i][4] = 'X'
					p = ' '.join(sorted([f'{i + 1}{abc[5 - where]}', f'{i + 1}E']))
					print(f'Passengers can take seats: {p}')
					success = True
		else:
			if side == 0:
				if d[i][where] == '.':
					d[i][where] = 'X'
					print(f'Passengers can take seats: {i + 1}{abc[where]}')
					success = True
			else:
				if d[i][5 - where] == '.':
					d[i][5 - where] = 'X'
					print(f'Passengers can take seats: {i + 1}{abc[5 - where]}')
					success = True
	if success:
		pr(d)
	else:
		print('Cannot fulfill passengers requirements')

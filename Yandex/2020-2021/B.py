
def ca(c, i):
	return chr(ord(c) + i * 3)


def __repstr__(s, i):
	return s[:i] + 'X' + s[i + 1:]


def repstr(_R, i):
	s = "ABCDEF".index(i)
	w = s % 3
	s = s // 3
	__R_ = _R.copy()
	__R_[s] = __repstr__(_R[s], w)
	return __R_


def pr(_D):
	for __I in _D:
		print(__I[0] + '_' + __I[1])


def repl(_D):
	for _F in _D:
		_F[0] = _F[0].replace('X', '#')
		_F[1] = _F[1].replace('X', '#')


n = int(input())
d = []
for i in range(n):
	d.append(input().split('_'))
m = int(input())
for i in range(m):
	c, s, w = input().split() # count, side, where
	c = int(c)
	s = 0 if s == 'left' else 1
	w = 0 if w == 'window' else 2
	if s == 1:
		w = 2 - w
	YES = False
	for j in range(n):
		if '.' * c in d[j][s] and d[j][s][w] == '.':
			print('Passengers can take seats: ', end='')
			if c == 3:
				p = [str(j + 1) + "ABCDEF"[s*3],
				     str(j + 1) + "ABCDEF"[s*3 + 1],
				     str(j + 1) + "ABCDEF"[s*3 + 2]]
			elif c == 2:
				p = [str(j + 1) + "ABCDEF"[s*3 + 1],
				     str(j + 1) + "ABCDEF"[s*3 + w]]
			else:
				p = [str(j + 1) + "ABCDEF"[s*3 + w]]
			p.sort()
			for k in p:
				d[j] = repstr(d[j], k[1])
			print(*p)
			YES = True
			pr(d)
			repl(d)
			break
	if not YES:
		print('Cannot fulfill passengers requirements')

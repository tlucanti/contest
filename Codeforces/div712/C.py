
def req(a, b, _a, _b, i):
	if i == n:
		if len(_a) == 0 and len(_b) == 0:
			return a, b
		else:
			return None
	if s[i] == '1':
		a1 = a.copy()
		b1 = b.copy()
		_a1 = _a.copy()
		_b1 = _b.copy()
		a2 = a.copy()
		b2 = b.copy()
		_a2 = _a.copy()
		_b2 = _b.copy()
	
		# ( + (
		_a1.append('(')
		_b1.append('(')
		a1.append('(')
		b1.append('(')
		if len(_a1) > n // 2 or len(_b1) > n // 2:
			pass
		else:
			ans = req(a1, b1, _a1, _b1, i + 1)
			if ans is not None:
				return ans 

		# ) + )
		if len(_a2) == 0 or len(_b2) == 0:
			pass
		else:
			_a2.pop()
			_b2.pop()
			a2.append(')')
			b2.append(')')
			ans = req(a2, b2, _a2, _b2, i + 1)
			if ans is not None:
				return ans
	else:
		a1 = a.copy()
		b1 = b.copy()
		_a1 = _a.copy()
		_b1 = _b.copy()
		a2 = a.copy()
		b2 = b.copy()
		_a2 = _a.copy()
		_b2 = _b.copy()
	
		# ( + )
		_a1.append('(')
		a1.append('(')
		if len(_a1) > n // 2:
			pass
		else:
			if len(_b1) == 0:
				pass
			else:
				_b1.pop()
				b1.append(')')
				ans = req(a1, b1, _a1, _b1, i + 1)
				if ans is not None:
					return ans
		# ) + (
		_b2.append('(')
		b2.append('(')
		if len(_b1) > n // 2:
			pass
		else:
			if len(_a2) == 0:
				pass
			else:
				_a2.pop()
				a2.append(')')
				ans = req(a1, b1, _a1, _b1, i + 1)
				if ans is not None:
					return ans


for t in range(int(input())):
	n = int(input())
	s = input()
	a = []
	b = []
	_a = []
	_b = []
	ans = req(a, b, _a, _b, 0)
	if ans is not None:
		print('YES')
		print(''.join(ans[0]))
		print(''.join(ans[1]))
	else:
		print('NO')

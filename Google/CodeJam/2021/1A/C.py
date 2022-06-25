
for t in range(int(input())):
	n, q = map(int, input().split())
	if n == 1:
		s = input()
		print(f'Case #{t + 1}: {s}/1')
	elif n == 2:
		r1, s1 = input().split()
		r2, s2 = input().split()
		s1, s2 = int(s1), int(s2)
		if s1 > s2:
			r1, s1, r2, s2 = r2, s2, r1, s1
		if s1 == 0 or s2 == 0:
			r = ''
			s = q
			for i in range(q):
				if r1[i] == 'T':
					r += 'F'
				else:
					r += 'T'
		else:
			s = s2
			r = r2
		print(f'Case #{t + 1}: {r} {s}/1')

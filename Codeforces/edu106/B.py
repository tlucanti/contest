
for t in range(int(input())):
	s = input()
	zz = s.count('00')
	oo = s.count('11')
	if zz == 0 or oo == 0:
		print('yes')
		continue
	if s.index('11') < s.rindex('00'):
		print('no')
	else:
		print('yes')

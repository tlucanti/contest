n = int(input())
st = set()
for i in range(n):
	s = input()[4:]
	if s == '000':
		print('3000')
	elif s == '3000':
		print('13000')
	elif s == '13000':
		print('113000')
	elif s == '113000':
		print('1113000')
	elif s == '1113000':
		print('11113000')
	elif s == '11113000':
		print('111113000')
	elif s == '111113000':
		print('1111113000')
	elif s == '9':
		print(1989)
	elif len(s) == 1:
		print(1990 + int(s))
	elif s == '99':
		print(1999)
	elif len(s) == 2:
		print(2000 + int(s))
	elif len(s) == 3:
		print(2000 + int(s))
	elif len(s) >= 4:
		if s[0] == '0' or s[0] == '1' or s[0] == '2':
			print('1' + s)
		else:
			print(s)
	else:
		print(s)

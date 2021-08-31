
num, den = map(int, input().split('/'))
num *= 1024 // den
for t in range(int(input())):
	s = input().split()
	n = int(s[0])
	ss = 0
	for i in range(1, n + 1):
		a, b = map(int, s[i].split('/'))
		a *= 1024 // b
		ss += a
	delay = num - ss
	delay = bin(delay)[2::]
	delay = '0' * (11 - len(delay)) + delay
	print(delay.count('1'), end=' ')
	for i in range(len(delay)):
		if int(delay[i]):
			print(f'1/{pow(2, i)}', end=' ')
	print()


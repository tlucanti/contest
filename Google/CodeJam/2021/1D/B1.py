
for t in range(int(input())):
	x, y, s = input().split()
	x, y = int(x), int(y)
	s = s.replace('?', '')
	print(f'Case #{t + 1}: {s.count("CJ") * x + s.count("JC") * y}')

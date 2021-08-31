
for t in range(int(input())):
	n, m, x = map(int, input().split())
	j = (x - 1) % n
	i = (x - 1) // n
	print(j * m + i + 1)


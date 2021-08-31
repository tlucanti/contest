
for t in range(int(input())):
	n = int(input())
	n1 = (n * 5) // 2
	if (n1 % 5):
		n1 += 5 - (n1 % 5)
	if (n1 < 15):
		n1 = 15
	print(n1)

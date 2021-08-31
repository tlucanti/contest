
for t in range(int(input())):
	a = input()
	b = input()
	ans = 0
	for i in range(len(a)):
		for j in range(len(a) + 1):
			if a[i:i + j] in b:
				ans = max(ans, len(a[i:i + j]))
	print(len(a) - ans + len(b) - ans)


for t in range(int(input())):
	n, k = map(int, input().split())
	if k == 0:
		print(*list(range(1, n + 1)))
		continue
	if k > (n - 1) // 2:
		print(-1)
		continue
	ptr = 0
	s = (n + 1) // 2
	a = []
	while k > 0:
		a.append(s - ptr)
		a.append(s + ptr + 1)
		ptr += 1
		k -= 1
	for i in range(s + ptr + 1, n + 1):
		a.append(i)
	for i in range(s - ptr, 0, -1):
		a.append(i)
	print(*a)

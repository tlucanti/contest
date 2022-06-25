
for t in range(int(input())):
	n, k1, k2 = map(int, input().split())
	w, b = map(int, input().split())
	w -= min(k1, k2)
	b -= n - max(k1, k2)
	if w > 0:
		w -= abs(k1 - k2) // 2
	if b > 0:
		b -= abs(k1 - k2) // 2
	if b <= 0 and w <= 0:
		print('yes')
	else:
		print('no')

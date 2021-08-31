
for t in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	# m = None
	# for i in range(n -1):
	# 	mi = (i + 1) * (i + 2) - k * (a[i] | a[i + 1])
	# 	if m is None:
	# 		m = mi
	# 	else:
	# 		m = max(m , mi)
	# print(m)


	# m = None
	#
	m1 = a[0]
	m2 = a[1]
	i1, i2 = 0, 1
	for i in range(2, n):
		if a[i] < m1:
			m1, m2 = a[i], m1
			i1, i2 = i, i1
		elif a[i] < m2:
			m2 = a[i]
			i2 = i
	# # print(i1, i2, m1, m2, (i1+1) * (i2+1) - k * (a[i1] | a[i2]))
	# # print((n-1)*n - k * (a[n-1]|a[n-2]))
	ans1 = (i1+1) * (i2+1) - k * (a[i1] | a[i2])
	print(i1, i2, ans1)
	# ans2 = (n-1)*n - k * (a[n-1]|a[n-2])
	# # print(max(ans1, ans2))
	# for i in range(n):
	# 	for j in range(i + 1, n):
	# 		if i == j:
	# 			continue
	# 		mi = (i + 1) * (j + 1) - k * (a[i] | a[j])
	# 		if m is None:
	# 			m = mi
	# 		else:
	# 			m = max(m, mi)
	# 		print(i+1, j+1, ':', a[i], '|', a[j], '=', a[i] | a[j], '->', mi)
	# print(m)
	# print('----')
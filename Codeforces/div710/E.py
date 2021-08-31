
for t in range(int(input())):
	n = int(input())
	q = list(map(int, input().split()))
	start = 0

	max_s = set()
	max_ptr = q[0]
	p_max = []

	min_s = set(q)
	min_ptr = 1
	p_min = []
	for i in range(n):
		if start != q[i]:
			max_ptr = q[i]
			max_s.update({q[i]})
			start = q[i]
			p_max.append(q[i])
			p_min.append(q[i])
		else:
			while max_ptr in max_s:
				max_ptr -= 1
			p_max.append(max_ptr)
			max_s.update({max_ptr})

			while min_ptr in min_s:
				min_ptr += 1
			p_min.append(min_ptr)
			min_ptr += 1
	print(*p_min)
	print(*p_max)


for t in range(int(input())):
	n = int(input())
	s = list(map(int, input().split()))
	# odd = {s[0]}   # нечетные
	# even = {s[1]}  # четные
	odd_m = s[0]
	odd_size = n
	even_m = s[1]
	even_size = n
	score = (s[0] + s[1]) * n
	score_min = score
	for i in range(2, n):
		if i % 2:
			if s[i] < even_m:
				score -= even_m * (even_size - 1)
				score += s[i] * (even_size - 1)
				even_size -= 1
				even_m = s[i]
			else:
				score -= even_m
				even_size -= 1
				score += s[i]
		else:
			if s[i] < odd_m:
				score -= odd_m * (odd_size - 1)
				score += s[i] * (odd_size - 1)
				odd_size -= 1
				odd_m = s[i]
			else:
				score -= odd_m
				odd_size -= 1
				score += s[i]
		score_min = min(score, score_min)
	print(score_min)

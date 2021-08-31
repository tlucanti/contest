
for t in range(int(input())):
	n = int(input())
	s = list(map(int, input().split()))
	cnt = 0
	for i in range(n - 1):
		m = min(s[i:])
		j = s[i:].index(m)
		j += i
		cnt += j - i + 1
		s[i:j + 1] = s[i:j + 1][::-1]
	print(f'Case #{t + 1}: {cnt}')

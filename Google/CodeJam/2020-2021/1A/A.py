
for t in range(int(input())):
	n = int(input())
	s = list(map(int, input().split()))
	ans = 0
	for i in range(1, n):
		while s[i] <= s[i - 1]:
			while len(str(s[i])) < len(str(s[i - 1])) - 1:
				if int(str(s[i - 1])[:len(str(s[i]))]) != s[i]:
					ii = 0
				else:
					ii = int(str(s[i - 1])[len(str(s[i]))])
				s[i] = s[i] * 10 + ii
				ans += 1
			if len(str(s[i])) == len(str(s[i - 1])) - 1:
				if int(str(s[i - 1])[:len(str(s[i]))]) != s[i]:
					ii = 0
				else:
					ii = s[i - 1] % 10
					if ii != 9:
						ii += 1
			else:
				ii = 0
			s[i] = s[i] * 10 + ii
			ans += 1
	print(*s)
	print(f'Case #{t + 1}: {ans}')


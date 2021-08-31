
for t in range(int(input())):
	n, k = map(int, input().split())
	s = input()
	i = 0
	ans = 0
	while i < len(s):
		if s[i] == '*':
			i += 1
			ans = 1
			break
		i += 1
	while i < n:
		if '*' in s[i:i + k]:
			i += s[i:i + k].rindex('*') + 1
			ans += 1
		else:
			break

	print(ans)

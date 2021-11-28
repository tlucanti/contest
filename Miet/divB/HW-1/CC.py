
n = int(input())
s = list(map(int, input().split()))
i = -1
score = 0
while i < n - 1:
	if s[i + 1] >= 0:
		score += s[i + 1]
		i += 1
	else:
		if i + 2 < n and s[i + 1] <= s[i + 2]:
			score += s[i + 2]
			i += 2
		else:
			score += s[i + 1]
			i += 1
print(score)

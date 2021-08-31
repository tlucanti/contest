
n = int(input())
s = list(map(int, input().split()))

srt = True
for i in range(n - 1):
	if s[i] > s[i + 1]:
		srt = False
		break
if srt:
	print(max(s) - min(s))
else:
	print(-1)

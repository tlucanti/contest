##
#	Author:		antikostya
#	Created:	2021-10-03 19:32:28
#	Modified:	2021-10-03 20:32:27
##

n = int(input())
balls = list(map(int, input().split()))
least = list(map(int, input().split()))
mn = balls[0] // least[0]
for i in range(n):
	mn = min(mn, balls[i] // least[0])
for _ in range(mn):
	for i in range(n):
		print((str(i) + ' ') * i)
	print():

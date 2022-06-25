##
#	Author:		antikostya
#	Created:	2021-10-02 11:36:02
#	Modified:	2021-10-02 14:14:53
##

WHITE = 1
BLACK = 2
EAT = BLACK

n, m = map(int, input().split())
mp = [[0] * m for i in range(n)]
w = int(input())
W = [None] * w
for i in range(w):
	ip = input().split()
	W[i] = list(map(int, ip))
	W[i] = [W[i][0] - 1, W[i][1] - 1]
	mp[W[i][0]][W[i][1]] = WHITE
del i
b = int(input())
B = [None] * b
for i in range(b):
	B[i] = list(map(int, input().split()))
	B[i] = [B[i][0] - 1, B[i][1] - 1]
	mp[B[i][0]][B[i][1]] = BLACK
del i
turn = input()
if turn == 'black':
	B, W = W, B
	b, w = w, b
	EAT = WHITE
for wt in W:
	for x in (-1, 1):
		for y in (-1, 1):
			xe = wt[0] + x
			ye = wt[1] + y
			xf = wt[0] + x + x
			yf = wt[1] + y + y
			if xf < 0 or xf >= n or yf < 0 or yf >= m:
				continue
			elif mp[xe][ye] == EAT and mp[xf][yf] == 0:
				print('Yes')
				exit(0)
print('No')

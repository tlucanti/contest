##
#	Author:		antikostya
#	Created:	2021-10-17 14:01:39
#	Modified:	2021-10-17 15:37:29
##

Y, X = map(int, input().split())
MAP = [None] * Y
gd = [[0] * X for _ in range(Y)]
for y in range(Y):
	MAP[y] = input()
for x in range(X):
	gd[0][x] = 1
for y in range(Y):
	gd[y][0] = 1
for x in range(1, X):
	for y in range(1, Y):
		if MAP[y][x] == 'X':
			continue
		gd[y][x] = int(gd[y - 1][x] or gd[y][x - 1])
col_def = [0] * X
for x in range(X):
	is_def = True
	for y in range(Y):
		if gd[y][x] and MAP[y][x] == 'X':
			is_def = False
			break
	if not is_def:
		col_def[x] = 1
bad_array = [0] * X
if 1 in col_def:
	last_bad = X - 1 - col_def[::-1].index(1)
else:
	last_bad = -1
for i in range(X - 1, -1, -1):
	if col_def[i]:
		last_bad = i
	bad_array[i] = last_bad

for _ in range(int(input())):
	l, r = map(int, input().split())
	l -= 1
	r -= 1
	if bad_array[l] < r:
		print('NO')
	else:
		print('YES')

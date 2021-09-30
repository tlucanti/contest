##
#	Author:		antikostya
#	Created:	2021-09-20 17:23:33
#	Modified:	2021-09-20 17:36:35
##

n = int(input())
m = 0
FOUND = False
for i in range(1, 74):
	for j in range(1, 74):
		_a = i*i*i + j*j*j
		FOUND = False
		if _a <= n and _a > m:
			for i1 in range(int(pow(_a, 1/3))):
				if FOUND:
					break
				if i1 == i or i1 == j:
					continue
				for i2 in range(int(pow(_a, 1/3))):
					if i2 == i or i2 == j:
						continue
					if i1*i1*i1 + i2*i2*i2 == _a:
						m = _a
						FOUND = True
						break

if m == 0:
	print(-1)
else:
	print(m)

##
#	Author:		antikostya
#	Created:	2021-11-27 13:34:45
#	Modified:	2021-11-27 13:43:49
##

def inp():
	return list(map(int, input().split()))

A = inp()
ok = ['NO', 'NO', 'NO']

srt = sorted(A)
for k in range(3):
	if A[k] == srt[1]:
		ok[k] = 'YES'

for i in range(3):
	for j in range(3):
		if i == j:
			continue
		a = A.copy()
		a[i] = a[i] - a[j]
		srt = sorted(a)
		for k in range(3):
			if a[k] == srt[1]:
				ok[k] = 'YES'
print('\n'.join(ok))

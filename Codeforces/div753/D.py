##
#	Author:		antikostya
#	Created:	2021-11-02 17:33:04
#	Modified:	2021-11-02 18:33:43
##

for _t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	s = input()
	R = []
	B = []
	for i in range(n):
		if s[i] == 'B':
			B.append(a[i])
		else:
			R.append(a[i])
	R.sort()
	B.sort()
	R.append(None)
	B.append(None)
	# print(R)
	# print(B)
	Ri = 0;
	Bi = 0
	ans = True
	for i in range(1, n + 1):
		if B[Bi] is not None and B[Bi] >= i:
			Bi += 1
			continue
		if R[Ri] is not None and R[Ri] <= i:
			Ri += 1
			continue
		ans = False
		break
	if ans:
		print('YES')
	else:
		print('NO')

##
#	Author:		antikostya
#	Created:	2021-12-19 12:00:53
#	Modified:	2021-12-19 12:07:21
##

a, b, c, d, e, f = [int(input()) for i in range(6)]
if f * d * b != a * e * c:
	print(-1)
else:
	A = c * b
	B = d * b
	C = a * c
	if A + B > C and A + C > B and B + C > A:
		print(1)
	else:
		print(-1)
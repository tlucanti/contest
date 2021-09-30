##
#	Author:		antikostya
#	Created:	2021-09-20 18:12:10
#	Modified:	2021-09-20 19:46:29
##

def time(h, m):
	return f'{h[0]}{h[1]}:{m[0]}{m[1]}'


def sign(z):
	if z >= 0:
		return 1
	elif z < 0:
		return -1

h1, m1 = map(lambda x: [int(x[0]), int(x[1])], input().split(':'))
h2, m2 = map(lambda x: [int(x[0]), int(x[1])], input().split(':'))
n = []
n.append(time(h1, m1))

if not (h1[0] > h2[0] and h1[0] == 2):
	# ones first
	dir = abs(h2[1] - h1[1]) > 5
	dir = (1 - dir) * 2 - 1
	dir = sign(h2[1] - h1[1]) * dir
	while (h1[1] != h2[1]):
		h1[1] += dir
		h1[1] %= 10
		n.append(time(h1, m1))
	#
	while (h1[0] != h2[0]):
		h1[0] += sign(h2[0] - h1[0])
		n.append(time(h1, m1))

else:
	# decs first
	while (h1[0] != h2[0]):
		h1[0] += sign(h2[0] - h1[0])
		n.append(time(h1, m1))
	#
	dir = abs(h2[1] - h1[1]) > 5
	dir = (1 - dir) * 2 - 1
	dir = sign(h2[1] - h1[1]) * dir
	while (h1[1] != h2[1]):
		h1[1] += dir
		h1[1] %= 10
		n.append(time(h1, m1))

while (m1[0] != m2[0]):
	m1[0] += sign(m2[0] - m1[0])
	n.append(time(h1, m1))

dir = abs(m2[1] - m1[1]) > 5
dir = (1 - dir) * 2 - 1
dir = sign(m2[1] - m1[1]) * dir
while (m1[1] != m2[1]):
	m1[1] += dir
	m1[1] %= 10
	n.append(time(h1, m1))

print(len(n))
print(*n, sep='\n')

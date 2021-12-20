##
#	Author:		antikostya
#	Created:	2021-12-16 16:30:23
#	Modified:	2021-12-16 16:41:51
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	s = input()
	t = input()
	a = s.count('a')
	b = s.count('b')
	c = s.count('c')
	s = s.replace('a', '')
	s = s.replace('b', '')
	s = s.replace('c', '')
	s = ''.join(sorted(s))
	if t == 'abc' and a * b * c != 0:
		print('a' * a + 'c' * c + 'b' * b + s)
	else:
		print('a' * a + 'b' * b + 'c' * c + s)



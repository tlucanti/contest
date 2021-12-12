##
#	Author:		antikostya
#	Created:	2021-11-28 17:20:23
#	Modified:	2021-11-28 18:17:18
##

def inp():
	return list(map(int, input().split()))

n, q = inp()
a = list(input())
abc = set()
for i in range(n - 2):
	if a[i] == 'a':
		if a[i + 1] == 'b':
			if a[i + 2] == 'c':
				abc.add(i)
for j in range(q):
	i, c = input().split()
	if n < 3:
		print(0)
		continue
	i = int(i)
	i -= 1
	a[i] = c
	if i in abc:
		if c != 'a':
			abc.remove(i)
	elif i - 1 in abc:
		if c != 'b':
			abc.remove(i - 1)
	elif i - 2 in abc:
		if c != 'c':
			abc.remove(i - 2)
	if ''.join(a[i:i+3]) == 'abc':
		abc.add(i)
	elif ''.join(a[i-1:i+2]) == 'abc':
		abc.add(i - 1)
	elif ''.join(a[i-2:i+1]) == 'abc':
		abc.add(i - 2)
	print(len(abc))

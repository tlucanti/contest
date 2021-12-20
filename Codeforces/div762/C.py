##
#	Author:		antikostya
#	Created:	2021-12-20 17:31:24
#	Modified:	2021-12-20 17:49:54
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	a, s = input().split()
	# a = '{a:0>{size}}'.format(size=len(s), a=a)
	# s = '{s:0>{size}}'.format(size=len(a), s=s)
	ans = ''
	j = len(s) - 1
	if int(a) > int(s):
		print(-1)
		continue
	for i in range(len(a) - 1, -1, -1):
		if j < 0 or j == 0 and int(s[j]) < int(a[i]):
			print(-1)
			ans = None
			break
		if int(s[j]) < int(a[i]):
			n = int(s[j - 1:j + 1]) - int(a[i])
			if n > 9 or n < 0:
				print(-1)
				ans = None
				break
			ans = str(n) + ans
			j -= 2
		else:
			n = int(s[j]) - int(a[i])
			if n > 9 or n < 0:
				print(-1)
				ans = None
				break
			ans = str(n) + ans
			j -= 1
	if ans is not None:
		ans = s[:j + 1] + ans
		if int(ans) == 0:
			print(0)
		else:
			print(ans.lstrip('0'))

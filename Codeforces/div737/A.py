##
#    author:  kostya
#    created: 2021-08-09 17:38:52
#    modified 2021-08-09 17:45:04
##

for t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	m = max(a)
	print((sum(a) - m) / (n-1) + m)
	

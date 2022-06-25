##
#	Author:		antikostya
#	Created:	2021-11-27 13:34:45
#	Modified:	2021-11-27 13:53:54
##

def inp():
	return list(map(int, input().split()))

n, m = inp()
glass = [''] * n
for i in range(n):
	glass[i] = input()
k = int(input())
booze = [None] * k
for i in range(k):
	booze[i] = input().split()
	booze[i][1] = int(booze[i][1])

i = n - 2 # glass
for j in range(k): # booze
	for l in range(booze[j][1]):
		glass[i] = glass[i].replace(' ', booze[j][2])
		i -= 1
print(*glass, sep='\n')

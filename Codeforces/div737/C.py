##
#    author:  kostya
#    created: 2021-08-09 18:19:20
#    modified 2021-08-09 19:26:43
##

from math import factorial as f

C = lambda n, k: f(n) // (f(k) * f(n-k))

for t in range(int(input())):
	n, k = map(int, input().split())
	ans = 0
	p = int(1e9) + 7
	for i in range(0, n+1, 2):
		ans = (ans + C(n, i) % p) % p
	print(pow(ans + n%2, k, mod=p))


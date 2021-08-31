##
#    author:  kostya
#    created: 2021-07-31 14:37:24
#    modified 2021-07-31 14:45:57
##

def d_sum(n):
	return sum(map(int, str(n)))


a, b, c = map(int, input().split())
ans = []
for i in range(83):
	x = b * pow(i, a) + c
	if x <= 0 or x >= int(1e9):
		continue
	if d_sum(x) == i:
		ans.append(x)
print(len(ans))
print(*ans)

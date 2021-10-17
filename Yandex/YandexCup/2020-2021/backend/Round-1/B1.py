##
#	Author:		antikostya
#	Created:	2021-10-02 12:52:27
#	Modified:	2021-10-02 14:30:38
##

class box(object):
	def __init__(self, del_id):
		self.del_id = del_id
		self.next = []


def dfs(mybox):
	for bx in boxes[mybox].next:
		st.add(boxes[bx].del_id)
		dfs(bx)


n = int(input())
delivery = list(map(int, input().split()))
parent = list(map(int, input().split()))
k = int(input())
out = list(map(int, input().split()))

boxes = [box(delivery[i]) for i in range(n)]
roots = []
for i in range(n):
	if parent[i] == 0:
		roots.append(i)
	else:
		boxes[parent[i] - 1].next.append(i)
out = set(out)
st = set()
ans = []
for rt in roots:
	st = {boxes[rt].del_id}
	dfs(rt)
	if len(st & out) == 0:
		ans.append(rt + 1)
print(len(ans))
print(*ans)

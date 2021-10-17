##
#	Author:		antikostya
#	Created:	2021-10-02 11:35:55
#	Modified:	2021-10-02 12:30:15
##

class box(object):
	def __init__(self, id, type, delivery):
		self.id = id
		self.type = type
		self.dl = delivery
		self.next = set()

	def __repr__(self):
		return ('{' + f'id: {self.id}, type: {self.type}, del: {self.dl}, '
			+ 'next: ' + str(set(self.next)) + '}')

	def __contains__(self, item):
		for nxt in self.next:
			if inc[nxt].dl == item:
				return True
		return False


n = int(input())
dl = list(map(int, input().split()))
pl = list(map(int, input().split()))
k = int(input())
ot = list(map(int, input().split()))

inc = [None for _I1 in range(n)]
for i in range(n):
	mybox = box(i, pl[i] == 0, dl[i])
	inc[i] = mybox
	if pl[i] != 0:
		inc[pl[i] - 1].next.add(mybox.id)

# for __pl in inc:
# 	print(__pl)

ans = []
for _pl in inc:
	if _pl.type:
		f = True
		for d in ot:
			if d in _pl:
				f = False
				break
		if f:
			ans.append(_pl.id + 1)
print(len(ans))
print(*ans)
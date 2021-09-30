##
#	Author:		kostya
#	Created:	2021-08-30 23:57:22
#	Modified:	2021-09-30 00:38:56
##

class Node(object):
	def __init__(self, c, term=False):
		self.c = c.lower()
		self.term = term
		self.next = []
		self.ans = "empty"
	def __lt__(self, other):
		return self.c < other.c
	def add(self, c, term):
		new = Node(c, term)
		for nd in self.next:
			if nd.c == c.lower():
				return nd
		self.next.append(new)
		self.next.sort()
		return new
	def add_string(self, st):
		ptr = self
		for c in st[1:-1]:
			ptr = ptr.add(c, False)
		ptr.add(st[-1], True).ans = st
	def go(self, c):
		for nd in self.next:
			if nd.c == c.lower():
				return nd
def dfs(root, counter):
	for nd in root.next:
		if counter == 0:
			return
		if nd.term:
			g_ans.append(nd.ans)
		counter = dfs(nd, counter - nd.term)
	return counter

def bfs(root, query):
	global g_ans
	for c in query[1:]:
		root = root.go(c)
		g_ans = []
		if root is None:
			print(g_ans)
			continue ;
		if root.term:
			g_ans.append(root.ans)
		dfs(root, 3 - root.term)
		print(g_ans)

__input = input()
__input = __input[__input.index('['):]
exec(f'lst = {__input}')
query = input()
query = query[query.index('"')+1:-1]
lst = [it for it in lst if it[:2].lower() == query[:2].lower()]
if len(query) < 2:
	exit(0)
trie = Node(query[0])
for st in lst:
	trie.add_string(st)
bfs(trie, query)

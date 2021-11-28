##
#    author:  kostya
#    created: 2021-08-29 13:45:21
#    modified 2021-08-29 15:54:24
##

class Node(object):

	def __init__(self, len, link=0, next=None):
		self.len = len
		self.link = link
		if next is None:
			self.next = dict()
		else:
			self.next = next.copy()

	def __repr__(self):
		return '{' + f'len={self.len}, link={self.link}, next={self.next}' + '}'


def suffix_automaton(s):

	nodes = [Node(0, -1)]
	last = 0

	for c in s:
		nodes.append(Node(nodes[last].len + 1))
		new = len(nodes) - 1
		p = last
		# print(nodes)
		while p != -1 and c not in nodes[p].next:
			nodes[p].next[c] = new
			p = nodes[p].link
		if p == -1:
			nodes[new].link = 0
		else:
			q = nodes[p].next[c]
			if nodes[p].len + 1 == nodes[q].len:
				nodes[new].link = q
			else:
				nodes.append(Node(nodes[p].len + 1,
					nodes[q].link, nodes[q].next))
				clone = len(nodes) - 1
				while p != -1 and nodes[p].next[c] == q:
					nodes[p].next[c] = clone
					p = nodes[p].link
				nodes[new].link = clone
				nodes[q].link = clone
		last = new
	return nodes


def issub(nd, s):
	v = 0
	for c in s:
		v = nd[v].next.get(c, -1)
		if v == -1:
			return 'NO'
	return 'YES'


s = input()
n = int(input())

nodes = suffix_automaton(s)
# print(nodes)
for i in range(n):
	s = input()
	print(issub(nodes, s))

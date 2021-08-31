/**
 *    author:  kostya
 *    created: 2021-08-29 15:20:51
 *    modified 2021-08-29 18:56:33
 **/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>


namespace tlucanti
{
	struct Node
	{
		int				len;
		int				link;
		std::unordered_map<int, int>	next;

		Node(int _len, int _link,
						std::unordered_map<int, int> *_next)
		{
			len = _len;
			link = _link;
			if (_next != nullptr)
			next = *_next;
		}

		Node(const Node &__cpy) = delete;
		Node(Node &&__mv) = default;
		Node &operator =(const Node &__cpy) = delete;
		Node &operator =(Node &&__mv) = default;
	};


	void suffix_automaton(const std::string &str,
							std::vector<Node> &nodes)
	{
		int	last;
		int	nw;
		int	p;
		int	q;
		int	clone;

		nodes.emplace_back(0, -1, nullptr);
		last = 0;

		for (char c : str)
		{
		nodes.emplace_back(nodes[last].len + 1, 0, nullptr);
		nw = (int)nodes.size() - 1;
		p = last;
		while (p != -1 and nodes[p].next.count(c) == 0)
		{
			nodes[p].next[c] = nw;
			p = nodes[p].link;
		}
		if (p == -1)
			nodes[nw].link = 0;
		else
		{
			q = nodes[p].next[c];
			if (nodes[p].len + 1 == nodes[q].len)
			nodes[nw].link = q;
			else
			{
			nodes.emplace_back(nodes[p].len + 1,
									nodes[q].link, &nodes[q].next);
			clone = (int)nodes.size() - 1;
			while (p != -1 and nodes[p].next[c] == q)
			{
				nodes[p].next[c] = clone;
				p = nodes[p].link;
			}
			nodes[nw].link = clone;
			nodes[q].link = clone;
			}
		}
		last = nw;
		}
	}


	bool issub(const std::vector<Node> &nodes,
				 const std::string &str)
	{
		int			v;
		v = 0;
		for (char c : str)
		{
		auto it = nodes[v].next.find(c);
		if (it == nodes[v].next.end())
			return false;
		v = it->second;
		}
		return true;
	}
}

int main()
{
	std::string	str;
	int	n;
	std::vector<tlucanti::Node>	nodes;

	std::cin >> str;
	std::cin >> n;
	tlucanti::suffix_automaton(str, nodes);
	while (n--)
	{
	std::cin >> str;
	std::cout << (issub(nodes, str) ? "YES\n" : "NO\n");
	}
	return 0;
}

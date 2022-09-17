
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <algorithm>

using namespace::std;

typedef unsigned long long ull;

const ull INF = (ull)1e18;

struct node
{
	int n;
	ull forward;
	ull backward;
	bool visited;

	node(int n)
		: n(n), forward(INF), backward(INF), visited(false)
	{}
};

struct edge
{
	int a;
	int b;
	int cost;

	edge(int a, int b, int c)
		: a(a), b(b), cost(c)
	{}

	edge()
		: a(), b(), cost()
	{}
};

void bfs_fwd(
	deque<node *> &q,
	const vector<vector<node *>> &inc,
	const map<pair<int, int>, int> &edges,
	const vector<node *> &nodes
)
{
	while (true)
	{
		if (q.empty())
			break ;
		node *front = q.front();
		front->visited = true;
		q.pop_front();
		
		for (node *nd : inc.at(front->n))
		{
			auto ed_it = edges.find(pair<int, int>(front->n, nd->n));
			ull ed = INF;

			if (ed_it != edges.end())
				ed = ed_it->second;
			nd->forward = min(nd->forward, front->forward + ed);
			if (nd->visited)
				continue ;
			q.push_back(nodes.at(nd->n));
		}
	}
}

void bfs_bwd(
	deque<node *> &q,
	const vector<vector<node *>> &inc_rev,
	const map<pair<int, int>, int> &edges,
	const vector<node *> &node
)
{
	while (true)
	{
		if (q.empty())
			break ;
		struct node *front = q.front();
		front->visited = true;
		q.pop_front();

		for (struct node *nd : inc_rev.at(front->n))
		{
			auto ed_it = edges.find(pair<int, int>(nd->n, front->n));
			ull ed = INF;
			
			if (ed_it != edges.end())
				ed = ed_it->second;
			nd->backward = min(
				min(nd->backward, front->forward + ed),
				min(front->backward + ed, nd->forward)
			);
			if (nd->visited)
				continue ;
			q.push_back(node.at(nd->n));
		}
	}
}

int main()
{
	int n, m;
	cin >> n >> m;

	vector<node *> nodes(n);
	for (int i=0; i < n; ++i)
		nodes.at(i) = (new node(i));
	nodes.at(0)->forward = 0;
	nodes.at(0)->backward = 0;

	vector<edge> v(m);
	for (int i=0; i < m; ++i)
	{
		int a, b, c;
		cin >> a >> b >> c;
		--a;
		--b;
		v.at(i) = edge(a, b, c);
	}
	
	sort(v.begin(), v.end(), [](const edge &a, const edge &b){ return a.cost < b.cost; });

	map<pair<int, int>, int> edges;
	for (const edge &e : v)
		edges[pair<int, int>(e.a, e.b)] = e.cost;

	vector<vector<node *>> inc(n);
	for (const edge &e : v)
		inc.at(e.a).push_back(nodes.at(e.b));

	vector<vector<node *>> inc_back(n);
	for (const edge &e : v)
		inc_back.at(e.b).push_back(nodes.at(e.a));

	deque<node *> q;

	q.push_back(nodes.at(0));
	bfs_fwd(q, inc, edges, nodes);

	for (node *_n : nodes)
		_n->visited = false;

	q.push_back(nodes.at(0));
	bfs_bwd(q, inc_back, edges, nodes);

	for (int i=1; i < n; ++i)
	{
		ull b = nodes.at(i)->backward;
		if (b == INF)
			cout << "-1 ";
		else
			cout << b << ' ';
	}
	cout << endl;
}



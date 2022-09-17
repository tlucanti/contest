
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <deque>

using namespace::std;


typedef unsigned long long ull;

struct edge
{
	ull a;
	ull b;
	ull cost;

	edge(ull a, ull b, ull cost) : a(a), b(b), cost(cost) {}
	edge() : a(), b(), cost() {}
};

const ull INF = (int)1e18;

struct node
{
	ull n;
	ull forward = INF;
	ull backward = INF;
	bool visited = false;

	node(ull n) : n(n) {}
};

void bfs_forward(deque<pair<node *, ull>> &q, const vector<vector<pair<node *, ull>>> &inc)
{
	while (true)
	{
		pair<node *, ull> p = q.front();
		q.pop_front();
		node *n = p.first;
		ull c = p.second;
		n->visited = true;
		for (pair<node *, ull> pp : inc.at(n->n))
		{
			node *e = pp.first;
			e->forward = min(e->forward, n->forward + c);
			if (e->visited)
				continue ;
			q.push_back(pp);
		}
	}
}


int main()
{
	int n, m;
	cin >> n >> m;

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
	vector<vector<pair<node *, ull>>> inc(n);
	vector<node *> nodes(n);
	for (int i=0; i < n; ++i)
		nodes.at(i) = new node(i);
	for (const auto &i : v)
		inc.at(i.a).push_back({nodes.at(i.b), i.cost});
	
	deque<pair<node *, ull>> q;
	q.push_back(pair<node *, ull>(nodes.at(0), inc.at(0).at(0).second));
	bfs_forward(q, inc);

	for (const node *n : nodes)
		cout << n->forward << ' ';
	cout << endl;
}


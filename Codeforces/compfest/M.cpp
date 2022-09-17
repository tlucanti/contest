
#include <iostream>
#include <vector>


using namespace::std;

struct edge
{
	int a;
	int b;
	int cost;
};

const int INF = 2147483647;

void ford_bellman(int n, int m, const vector<edge> &e, vector<int> &d)
{
	(void)n;
	while (true)
	{
		bool any = false;
		for (int j=0; j < m; ++j)
		{
			if (d.at(e.at(j).a) < INF)
			{
				if (d.at(e.at(j).b) > d.at(e.at(j).a) + e.at(j).cost)
				{
					d.at(e.at(j).b) = d.at(e.at(j).a) + e.at(j).cost;
					any = true;
				}
			}
		}
		if (not any)
			break ;
	}
}

int main()
{
	vector<edge> e;
	vector<edge> e_rev;

	int vert, edges;

	cin >> vert >> edges;
	vector<vector<pair<int, int>>> inc_list(vert);

	for (int i=0; i < edges; ++i)
	{
		int a, b, cost;
		cin >> a >> b >> cost;
		--a;
		--b;
		e.push_back((edge){a, b, cost});
	}

	for (const auto &el : e)
	{
		e_rev.push_back((edge){el.b, el.a, el.cost});
		inc_list.at(el.a).push_back({el.b, el.cost});
	}

	//int v = 0;
	vector<int> d(vert, INF);
	vector<int> d_rev(vert, INF);
	d.at(0) = 0;
	d_rev.at(0) = 0;

	ford_bellman(vert, edges, e, d);
	ford_bellman(vert, edges, e_rev, d_rev);

	vector<int> res(vert - 1, 0);
	
	for (int num=1; num < vert; ++num)
	{
		int nm = num;
		int cur = 0;
		while (d.at(nm) >= d_rev.at(nm))
		{
			int min_d = d.at(nm);
			for (const auto &item : inc_list.at(num))
				min_d = min(min_d, d.at(item.first) + item.second);
			if (min_d == d.at(nm))
				break ;
			for (const auto &item : inc_list.at(num))
			{
				if (d.at(item.first) + item.second == min_d)
				{
					cur += item.second;
					nm = item.first;
					break ;
				}
			}
		}
		if (d.at(nm) == INF)
			res.at(num-1) = -1;
		else
			res.at(num-1) = d.at(nm) + cur;
	}
	
	for (int i : res)
		cout << i << ' ';
	cout << endl;
}



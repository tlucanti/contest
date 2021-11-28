/**
 *	Author:		antikostya
 *	Created:	2021-11-25 19:50:32
 *	Modified:	2021-11-25 20:22:02
 **/

#include <vector>
#include <set>
#include <iostream>

using namespace::std;

vector<vector<int>> inc;
set<int> fr;
vector<int> path;

int dfs1(int p, int parent)
{
	if (fr.contains(p))
		return 0;
	int steps = -1;
	for (int i : inc[p])
	{
		if (i == parent)
			continue;
		int branch = dfs1(i, p);
		if (branch != -1)
		{
			if (steps == -1)
				steps = branch + 1;
			else
				steps = min(steps, branch + 1);
		}
	}
	path[p] = steps;
	return steps;
}

void dfs2(int p, int parent)
{
	if (path[p] == -1)
		path[p] = path[parent] + 1;
	else
		path[p] = min(path[p], path[parent] + 1);
	for (int i : inc[p])
	{
		if (i == parent)
			continue;
		dfs2(i, p);
	}
}

bool dfs3(int p, int parent, int turn)
{
	if (inc[p].size() == 1 and turn < path[p] and p != 0)
		return true;
	for (int i : inc[p])
	{
		if (i == parent)
			continue;
		bool ok = dfs3(i, p, turn + 1);
		if (ok)
			return true;
	}
	return false;
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, k;
		cin >> n >> k;
		fr.clear();
		for (int i=0; i < k; ++i)
		{
			int _i;
			cin >> _i;
			fr.insert(_i - 1);
		}
		inc.resize(0);
		inc.resize(n);
		for (int i=0; i < n - 1; ++i)
		{
			int _a, _b;
			cin >> _a >> _b;
			--_a;
			--_b;
			inc[_a].push_back(_b);
			inc[_b].push_back(_a);
		}
		path.resize(0);
		path.resize(n, -1);
		for (int f : fr)
			path[f] = 0;
		dfs1(0, 0);
		dfs2(0, 0);
		if (dfs3(0, 0, 0))
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	return 0;
}

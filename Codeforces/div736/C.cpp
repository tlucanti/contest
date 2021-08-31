/**
 *    author:  kostya
 *    created: 2021-08-01 18:13:03
 *    modified 2021-08-01 18:52:24
 **/

#include <bits/stdc++.h>
using namespace::std;
#define ll long long

int main()
{
	int d;
	int m, n;
	int u, v;
	int cnt = 0;
	cin >> n >> m;
	vector<set<int>>inc(n);
	for (int i=0;i<m;++i) {
		cin >> u >> v;
		if (u > v)
			swap(u, v);
		if (inc[u].empty())
			++cnt;
		inc[u].emplace(v);
	}
	cin >> m;
	for (int i=0;i<m;++i) {
		cin >> d;
		if (d == 3)
			cout << n - cnt << endl;
		else {
			cin >> u >> v;
			if (u > v)
				swap(u, v);
			if (d == 1) {
				if (inc[u].empty())
					++cnt;
				inc[u].emplace(v);
			} else {
				inc[u].erase(v);
				if (inc[u].empty())
					--cnt;
			}
		}
	}
	return 0;
}


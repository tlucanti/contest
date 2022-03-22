/*
* @Author: tlucanti
* @Date:   2022-03-20 15:35:50
* @Last Modified by:   tlucanti
* @Last Modified time: 2022-03-20 16:13:28
*/

#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace::std;

typedef unsigned long long ull;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		vector<ull> a(n);
		for (int i=0; i < n; ++i)
			cin >> a[i];
		sort(a.begin(), a.end());
		multiset<ull> b;
		ull sm = 0;
		for (ull i : a)
			sm += i;
		b.insert(sm);
		bool ok = true;
		while (not b.empty())
		{
			if (*--b.end() < a.back())
			{
				ok = false;
				break ;
			}
			while (not a.empty() and not b.empty() and
				   (*--b.end()) == a.back())
			{
				a.pop_back();
				b.erase(--b.end());
			}
			if (b.empty())
				break ;
			if ((*--b.end()) > 1)
			{
				ull p2 = (*--b.end()) / 2;
				ull p1 = (*--b.end()) - p2;
				b.erase(--b.end());
				b.insert(p1);
				b.insert(p2);
			}
		}
		cout << (ok ? "YES" : "NO") << endl;
	}
}

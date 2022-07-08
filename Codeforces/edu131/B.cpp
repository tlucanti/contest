
#include <iostream>
#include <vector>
#include <set>

using namespace::std;

typedef unsigned long long ull;

int main()
{
	ull t;
	cin >> t;
	while (t--)
	{
		ull n;
		cin >> n;
		set<ull> av;
		for (ull i=2; i <= n; ++i)
		{
			av.insert(i);
		}
		vector<ull> ans(n, 0);
		ans[0] = 1;
		ull d = 0;
		ull prev = 0;
		for (ull i=1; i < n; ++i)
		{
			if (av.count(prev * 2) > 0)
			{
				ans[i] = prev * 2;
				av.erase(prev * 2);
				prev *= 2;
				d += 1;
			}
			else
			{
				ull m;
				m = *(av.begin());
				ans[i] = m;
				av.erase(m);
				prev = m;
			}
		}
		cout << 2 << endl;
		for (ull i=0; i < n; ++i)
		{
			cout << ans[i] << ' ';
		}
		cout << endl;
	}
}

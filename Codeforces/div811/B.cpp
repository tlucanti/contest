
#include <iostream>
#include <map>
#include <vector>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		vector<int> a(n);
		map<int, int> d;
		for (int i=0; i < n; ++i)
			cin >> a.at(i);
		for (int i : a)
		{
			if (d.count(i) == 0)
				d[i] = 0;
			d[i] += 1;
		}
		int remaining = 0;
		for (const auto &i : d)
			if (i.second > 1)
				++remaining;
		int ans = 0;
		for (int i : a)
		{
			if (remaining == 0)
				break ;
			if (d[i] == 2)
			{
				--d[i];
				--remaining;
			}
			if (d[i] > 1)
				--d[i];
			++ans;
		}
		cout << ans << endl;
	}
}


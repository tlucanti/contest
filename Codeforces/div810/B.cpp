
#include <vector>
#include <iostream>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		long long n, m;
		cin >> n >> m;
		vector<long long> a(n);
		for (int i=0; i < n; ++i)
			cin >> a.at(i);
		vector<vector<long long>> inc(n);
		for (int i=0; i < m; ++i)
		{
			long long ai, bi;
			cin >> ai >> bi;
			--ai;
			--bi;
			inc.at(ai).push_back(bi);
			inc.at(bi).push_back(ai);
		}
		if (m % 2 == 0)
		{
			cout << 0 << endl;
			continue ;
		}
		long long sm = 0;
		for (int i=0; i < n; ++i)
			sm += a.at(i);
		long long oddmin = sm;
		for (int i=0; i < n; ++i)
		{
			if (inc.at(i).size() % 2)
				oddmin = min(oddmin, a.at(i));
		}
		long long evenmin = sm;
		for (int i=0; i < n; ++i)
		{
			if (inc.at(i).size() % 2 == 0)
			{
				for (long long j : inc.at(i))
				{
					if (inc.at(j).size() % 2 == 0)
						evenmin = min(evenmin, a.at(i) + a.at(j));
				}
			}
		}
		cout << min(oddmin, evenmin) << endl;
	}
}


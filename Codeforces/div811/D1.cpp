
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace::std;

bool srt_fun(const vector<int> &a, const vector<int> &b)
{
	pair<int, int> aa(a.at(0), a.at(1));
	pair<int, int> bb(b.at(0), b.at(1));
	return aa > bb;
}

int main()
{
	int tt;
	cin >> tt;
	while (tt--)
	{
		string t;
		cin >> t;
		int n;
		cin >> n;
		vector<string> ss(n);
		vector<vector<int>> s;
		for (int i=0; i < t.size(); ++i)
		{
			for (int j=0; j < n; ++j)
			{
				if (t.substr(i, 1000).rfind(ss.at(j), 0) == 0)
				{
					vector<int> g(3);
					g.at(0) = i;
					g.at(1) = i + ss.at(j).size();
					g.at(2) = j;
				}
			}
		}
		sort(s.begin(), s.end(), srt_fun);
		int end = 0;
		int i = 0;
		bool ok = true;
		vector<pair<int, int>> ans;
		while (true)
		{
			if (end >= t.size())
				break ;
			if (i >= s.size() or s.at(i).at(0) > end)
			{
				ok = false;
				break ;
			}
			for (int ii=i + 1; ii < s.size(); ++ii)
			{
				if (s.at(ii).at(0) <= end)
					i = ii;
			}
			ans.emplace_back(s.at(i).at(2) + 1, s.at(i).at(0) + 1);
		}

		if (not ok)
			cout << "-1\n";
		else
		{
			cout << ans.size() << endl;
			for (auto qwe : ans)
				cout << qwe.first << ' ' << qwe.second << endl;
		}
	}
}


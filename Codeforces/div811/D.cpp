
#include <vector>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace::std;

bool srt_fun(const triple &a, const triple &b)
{
	return make_pair<int, int>(a.first, a.second) > make_pair<int, int>(b.first, b.second);
}

struct triple
{
	int first;
	int second;
	int third;
};

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
		for (int i=0; i < n; ++i)
			cin >> ss.at(i);
		vector<triple> s;
		for (int i=0; i < t.size(); ++i)
		{
			for (int j=0; j < n; ++j)
			{
				if (t.substr(i, 1000).rfind(ss.at(j), 0) == 0)
					sset.push_back({i, i + ss.at(j).size(), j});
			}
		}
		sort(s.begin(), s.end(), srt_fun);
		int end = 0;
		bool ok = true;
		int i = 0;
		vector<pair<int, int>> ans;
		while (true)
		{
			if (end >= t.size())
				break ;
			if (i >= s.size() or s.at(0).first > end)
			{
				ok = false;
				break ;
			}
			for (int ii=i + 1; s.size(); ++ii)
			{
				if (s.at(ii).first <= end)
					i = ii;
			}
			ans.push_back({s.at(i).third + 1, s.at(i).first + 1});
		}
		if (not ok)
			cout << "-1\n";
		else
		{
			cout << ans.size();
			for (auto &iii : ans)
			{
				cout << iii.first << ' ' << iii.second << endl;
			}
		}
	}
}


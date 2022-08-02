
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace::std;

int main()
{
	int q;
	cin >> q;
	while (q--)
	{
		string t;
		cin >> t;
		int n;
		cin >> n;
		vector<string> ss(n);
		for (int i=0; i < n; ++i)
			cin >> ss.at(i);
		set<vector<int>> st;
		for (int i=0; i < t.size(); ++i)
		{
			for (int j=0; j < n; ++j)
			{
				if (t.substr(i, 1000).starts_with(ss.at(j)))
				{
					vector<int> ins = {i, static_cast<int>(i + ss.at(j).size()), j};
					st.insert(ins);
				}
			}
		}
		vector<vector<int>> s(st.begin(), st.end());
		sort(s.begin(), s.end(), [](
					const vector<int> &a, const vector<int> &b)
				{
					vector<int> aa = {a.at(0), a.at(1)};
					vector<int> bb = {b.at(0), b.at(1)};
					return aa < bb;
					});
		int end = 0;
		int i = 0;
		bool ok = true;
		vector<vector<int>> ans;
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
			vector<int> ins = {s.at(i).at(2) + 1, s.at(i).at(0) + 1};
			ans.push_back(ins);
			end = s.at(i).at(1);
		}

		if (not ok)
			cout << "-1\n";
		else
		{
			cout << ans.size() << endl;
			for (const auto &a : ans)
			{
				cout << a.at(0) << ' ' << a.at(1) << endl;
			}
		}
	}
}


/*
* @Author: kostya
* @Date:   2021-11-14 00:04:34
* @Last Modified by:   kostya
* @Last Modified time: 2021-11-14 15:48:46
*/

#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace::std;

bool in(const string &st, char target)
{
	for (char c : st)
		if (c == target)
			return true;
	return false;
}

void wrap(const string &s, vector<pair<char, int>> &wr)
{
	if (s.empty())
		return;
	wr.push_back({s[0], 1});
	for (int i=1; i < s.size(); ++i)
	{
		if (s[i] == wr.back().first)
			++wr.back().second;
		else
			wr.push_back({s[i], 1});
	}
}

bool unique(char a, char b, char c)
{
	return a != b and a != c and b != c;
}

int main()
{
	int n;
	cin >> n;
	while (n--)
	{
		string s;
		cin >> s;
		if (not (in(s, '1') and in(s, '2') and in(s, '3')))
		{
			cout << 0 << endl;
			continue;
		}
		int ans = s.size();
		vector<pair<char, int>> wr;
		wrap(s, wr);
		for (int i=1; i < wr.size() - 1; ++i)
		{
			if (unique(wr[i - 1].first, wr[i].first, wr[i + 1].first))
				ans = min(ans, wr[i].second + 2);
		}
		cout << ans << endl;
	}
}

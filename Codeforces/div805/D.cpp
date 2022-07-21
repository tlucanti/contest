
#include <iostream>
#include <string>
#include <algorithm>

using namespace::std;

bool cmp(char a, char b)
{
	return a > b;
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		string a;
		cin >> a;
		int p;
		cin >> p;
		string ps = a;
		sort(ps.begin(), ps.end(), cmp);
		int cost = 0;
		for (char c : a)
			cost += c - 'a' + 1;
		int deleted[26] = {};
		for (char c : ps)
		{
			if (cost <= p)
				break ;
			deleted[c - 'a'] += 1;
			cost -= c - 'a' + 1;
		}
		for (char c : a)
		{
			if (deleted[c - 'a'] > 0)
			{
				deleted[c - 'a'] -= 1;
				continue ;
			}
			cout << c;
		}
		cout << endl;
	}
}


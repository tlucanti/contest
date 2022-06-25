/**
 *	Author:		antikostya
 *	Created:	2022-01-03 18:27:53
 *	Modified:	2022-01-03 18:42:44
 **/

#include <map>
#include <iostream>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		map<pair<int, int>, int> it;

		int n;
		cin >> n;

		int min_l = -1, max_r = -1;
		int lc = -1, rc = -1;

		for (int i=0; i < n; ++i)
		{
			int l, r, c;
			cin >> l >> r >> c;

			if (min_l == -1 or l < min_l)
			{
				min_l = l;
				lc = c;
			}
			else if (l == min_l)
				lc = min(c, lc);

			if (max_r == -1 or r > max_r)
			{
				max_r = r;
				rc = c;
			}
			else if (r == max_r)
				rc = min(c, rc);

			if (it.count({l, r}))
				it[{l, r}] = min(it[{l, r}], c);
			else
				it[{l, r}] = c;

			if (it.count({min_l, max_r}))
			{
				cout << min(it[{min_l, max_r}], lc + rc) << endl;
			}
			else
			{
				cout << lc + rc << endl;
			}
		}
	}
}

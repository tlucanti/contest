/*
* @Author: kostya
* @Date:   2021-11-14 00:28:50
* @Last Modified by:   kostya
* @Last Modified time: 2021-11-14 15:54:35
*/

#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		map<int, int> d;
		int n, k;
		cin >> n >> k;
		vector<int> a(n);
		vector<int> srt(n);
		for (int i=0; i < n; ++i)
		{
			cin >> a[i];
			srt[i] = a[i];
		}
		sort(srt.begin(), srt.end());
		for (int i=0; i < n; ++i)
			d[srt[i]] = i;
		int s_i = d[a[0]];
		int ans = 1;
		for (int a_i=0; a_i < n; ++a_i)
		{
			if (s_i >= n or a[a_i] != srt[s_i])
			{
				++ans;
				s_i = d[a[a_i]];
			}
			++s_i;
		}
		if (ans <= k)
			cout << "Yes" << endl;
		else
			cout << "No" << endl;
	}
}

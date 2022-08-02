
#include <iostream>
#include <algorithm>
#include <vector>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, H, M;
		cin >> n >> H >> M;
		int tt = H * 60 + M;
		vector<int> v(n);
		for (int i=0; i < n; ++i)
		{
			int h, m;
			cin >> h >> m;
			v.at(i) = h * 60 + m;
		}
		sort(v.begin(), v.end(), [](int a, int b) { return a < b; });
		bool ok = false;
		int ans;
		for (int i=0; i < n; ++i)
		{
			if (v.at(i) >= tt)
			{
				ans = v.at(i) - tt;
				ok = true;
				break ;
			}
		}
		if (not ok)
			ans = v.at(0) + 60 * 24 - tt;
		cout << (ans / 60) << ' ' << (ans % 60) << endl;
	}
}


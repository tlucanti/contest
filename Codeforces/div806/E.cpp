
#include <iostream>
#include <vector>
#include <string>

using namespace::std;

void rotate(int &x, int &y, int n)
{
	int xx = x;
	x = n - y - 1;
	y = xx;
}

int main()
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		int n;
		cin >> n;
		vector<string> m(n);
		for (int y=0; y < n; ++y)
		{
			cin >> m[y];
			for (auto &c : m[y])
				c -= '0';
		}
		int ans = 0;
		for (int x=0; x < n; ++x)
		{
			for (int y=0; y < n; ++y)
			{
				int z = 0;
				z += m[y][x]; // 1
				int xx = x;
				int yy = y;
				rotate(xx, yy, n);
				z += m[yy][xx]; // 2
				rotate(xx, yy, n);
				z += m[yy][xx]; // 3
				rotate(xx, yy, n);
				z += m[yy][xx]; // 4
				ans += std::min(z, 4 - z);
			}
		}
		cout << ans / 4 << endl;
	}
}



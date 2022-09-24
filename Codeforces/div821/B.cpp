
#include <iostream>
using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, x, y;
		cin >> n >> x >> y;
		if (x * y != 0)
		{
			cout << "-1\n";
			continue ;
		}
		x = max(x, y);
		if (x == 0 or (n - 1) % x != 0)
		{
			cout << "-1\n";
			continue ;
		}
		int i=1;
		while (i < n)
		{
			for (int j=0; j < x; ++j)
				cout << i + 1 << ' ';
			i += x;
		}
		cout << endl;
	}
}


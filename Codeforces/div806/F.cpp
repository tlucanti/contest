
#include <iostream>
#include <vector>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		int n;
		cin >> n;
		vector<long long> a(n);
		for (int i=0; i < n; ++i)
		{
			cin >> a[i];
		}
		vector<long long> ok(n);
		for (int i=0; i < n; ++i)
		{
			if (a[i] < i + 1)
				ok[i] = 1;
		}
		vector<long long> cm(n);
		cm[0] = ok[0];
		for (int i=1; i < n; ++i)
		{
			cm[i] = ok[i] + cm[i - 1];
		}
		long long ans = 0;
		for (int i=2; i < n; ++i)
		{
			if (a[i] - 2 < 0 or a[i] - 2 >= n)
				continue ;
			ans += ok[i] * cm[a[i] - 2];
		}
		cout << ans << endl;
	}
}


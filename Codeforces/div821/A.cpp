
#include <iostream>
#include <vector>
using namespace::std;
int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, k;
		cin >> n >> k;
		vector<int> a(n);
		for (int i=0; i < n; ++i)
			cin >> a.at(i);
		long long ans = 0;
		for (int i=0; i < k; ++i)
		{
			int m = 0;
			for (int j=i; j < n; j += k)
				m = max(m, a[j]);
			ans += m;
		}
		cout << ans << endl;
	}
}


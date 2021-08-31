#include <iostream>
#include <string>

uint64_t x = 1000000007;
using namespace::std;


int main()
{
	uint64_t t, n, m;
	uint64_t d[10];
	uint64_t dc[10];

	cin >> t;
	while (t--)
	{
		cin >> n >> m;
		string nstr = to_string(n);
		for (int i=0; i < 10; ++i)
		{
			d[i] = 0;
			dc[i] = 0;
		}
		for (auto i : nstr)
		{
			i -= 48;
			d[i]++;
		}
		for (uint64_t i=0; i < m; ++i)
		{
			for (int j=0; j < 10; ++j)
			{
				dc[j] = d[(j + 9) % 10];
			}
			dc[1] = (dc[1] + d[9]) % x;
			for (int j=0; j < 10; ++j)
			{
				d[j] = dc[j];
			}
		}
		uint64_t ans = 0;
		for (int i=0; i < 10; ++i)
		{
			ans = (ans + d[i]) % x;
		}
		cout << ans << endl;
	}
}
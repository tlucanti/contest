
#include <iostream>
#include <vector>
#include <string>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		int n;
		cin >> n;
		vector<int> s(n);
		for (int i=0; i < n; ++i)
			cin >> s[i];
		for (int i=0; i < n; ++i)
		{
			int nn;
			cin >> nn;
			int ans = s[i];
			string ss;
			cin >> ss;
			for (char c : ss)
			{
				if (c == 'U')
					--ans;
				else
					++ans;
			}
			ans += 100;
			cout << (ans % 10) << ' ';
		}
		cout << endl;
	}
}


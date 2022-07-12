
#include <iostream>
#include <set>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		int n;
		cin >> n;
		set<char> s;
		int ans = 0;
		for (int i=0; i < n; ++i)
		{
			char a;
			cin >> a;
			if (s.count(a) > 0)
				++ans;
			else
				ans += 2;
			s.insert(a);
		}
		cout << ans << endl;
	}
}


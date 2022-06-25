
#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace::std;

bool check_pal(int x)
{
	int h = x / 60;
	int m = x % 60;
	char buf[100];
	sprintf(buf, "%02i:%02i", h, m);
	string s1 = buf;
	string s2 = buf;
	reverse(s2.begin(), s2.end());
	return s1 == s2;
}

int main()
{
	int _t;
	cin >> _t;
	while (_t--)
	{
		int h;
		int m;
		char c;
		int x;
		cin >> h >> c >> m >> x;
		int t = h * 60 + m;
		int t0 = t;
		int ans = 0;
		while (true)
		{
			ans += check_pal(t);
			t = (t + x) % (24 * 60);
			if (t == t0)
				break;
		}
		cout << ans << endl;
	}
}


#include <iostream>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int s;
		cin >> s;
		string ans;
		int next = 9;
		while (s > 0)
		{
			if (s > next)
			{
				ans = static_cast<char>(next + '0') + ans;
				s -= next;
				--next;
			}
			else
			{
				ans = static_cast<char>(s + '0') + ans;
				s = 0;
			}
		}
		cout << ans << endl;
	}
}

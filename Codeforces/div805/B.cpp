
#include <iostream>
#include <set>
#include <string>

using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		string a;
		cin >> a;
		set<int> s;
		int ans = 0;
		for (char c : a)
		{
			if (s.count(c) > 0)
				continue ;
			else if (s.size() == 3)
			{
				++ans;
				s.clear();
				s.insert(c);
			}
			else
				s.insert(c);
		}
		cout << ++ans << endl;
	}
}

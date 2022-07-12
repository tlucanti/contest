
#include <iostream>
#include <string>
#include <set>
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
		vector<string> a(n);
		for (int i=0; i < n; ++i)
			cin >> a[i];
		set<string> s;
		for (auto & i : a)
			s.insert(i);
		for (auto & i : a)
		{
			bool ok = false;
			for (int j=1; j < i.size(); ++j)
			{
				string q1 = i.substr(0, j);
				string q2 = i.substr(j, i.size());
				if (s.count(q1) > 0 and s.count(q2) > 0)
				{
					ok = true;
					break;
				}
			}
			if (ok)
				cout << 1;
			else
				cout << 0;
		}
		cout << endl;
	}
}


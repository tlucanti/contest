#include <iostream>
#include <vector>
using namespace::std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		vector<int> a(n);
		vector<int> s(n);
		for (int i=0; i < n; ++i)
			cin >> a.at(i);
		s.at(0) = a.at(0);
		for (int i=1; i < n; ++i)
		{
			if (s.at(i - 1) - a.at(i) < 0 or a.at(i) == 0)
				s.at(i) = s.at(i - 1) + a.at(i);
			else
			{
				s = {-1};
				break ;
			}

		}
		for (int i : s)
			cout << i << ' ';
		cout << endl;
	}
}

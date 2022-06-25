
#include <iostream>
#include <set>

using namespace::std;

int main()
{
	int _t;
	cin >> _t;
	while (_t--)
	{
		int n;
		cin >> n;
		set<int> s;
		int nn = n;
		while (nn--)
		{
			int a;
			cin >> a;
			s.insert(a);
		}
		int ns = s.size();
		cout << ns - (n - ns) % 2 << endl;
	}
}

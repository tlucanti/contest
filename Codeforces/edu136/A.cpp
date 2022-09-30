
#include <iostream>
using namespace::std;
int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, m;
		cin >> n >> m;
		cout << min(2, n) << ' ' << min(2, m) << endl;
	}
}

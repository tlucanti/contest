
#include <iostream>

using namespace::std;

int main()
{
	int _t;

	cin >> _t;
	while (_t--)
	{
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		cout << (b > a) + (c > a) + (d > a) << endl;
	}
}


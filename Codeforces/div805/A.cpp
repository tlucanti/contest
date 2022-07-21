
#include <iostream>

using namespace::std;


int dn(int n)
{
	if (n == 0)
		return 1;
	int d = 0;
	while (n)
	{
		n /= 10;
		++d;
	}
	return d;
}

int pow10(int n)
{
	int a = 1;
	while (n--)
		a *= 10;
	return a;
}

int main()
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		int n;
		cin >> n;
		if (n == 1)
		{
			cout << 0 << endl;
			continue;
		}
		int k = dn(n) - 1;
		cout << n - pow10(k) << endl;
	}
}

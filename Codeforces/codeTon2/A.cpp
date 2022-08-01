
#include <iostream>
#include <vector>
#include <string>

using namespace::std;


bool endswith(const string &a, const string &b)
{
	if (a.size() < b.size())
		return false;
	for (int i=0; i < b.size(); ++i)
	{
		if (b.at(b.size() - i - 1) != a.at(a.size() - i - 1))
			return false;
	}
	return true;
}

bool in(const string &a, char c)
{
	for (char cc : a)
		if (cc == c)
			return true;
	return false;
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int na, nb;
		cin >> na >> nb;
		string a, b;
		cin >> a >> b;
		if (nb > na)
		{
			cout << "NO\n";
			continue ;
		}
		if (na == 1)
		{
			if (a.at(0) == b.at(nb - 1))
				cout << "YES\n";
			else
				cout << "NO\n";
			continue ;
		}
		if (endswith(a, b.substr(1, 1e10)))
		{
			if (b[0] == '0')
			{
				if (in(a.substr(0, na - nb + 1), '0'))
					cout << "YES\n";
				else
					cout << "NO\n";
			}
			else
			{
				if (in(a.substr(0, na - nb + 1), '1'))
					cout << "YES\n";
				else
					cout << "NO\n";

			}
		}
		else
			cout << "NO\n";
	}
}


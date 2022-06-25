
#include <iostream>
#include <vector>
#include <string>

using namespace::std;

bool eq6(int a1, int a2, int a3, int a4, int a5, int a6)
{
	return (a1 == a2 and a2 == a3 and a3 == a4 and a4 ==a5 and a5 == a6);
}

int main()
{
	int _t;
	cin >> _t;
	while (_t--)
	{
		vector<string> m(8);
		for (int i=0; i < 8; ++i)
		{
			cin >> m[i];
		}
		for (int i=1; i < 7; ++i)
		{
			for (int j=1; j < 7; ++j)
			{
				if (eq6(m[i][j], m[i + 1][j + 1], m[i - 1][j - 1], m[i + 1][j - 1], m[i - 1][j + 1], '#'))
				{
					cout << i + 1 << ' ' << j + 1 << endl;
					goto OUT;
				}
			}
		}
OUT:
	int _;

	}
}

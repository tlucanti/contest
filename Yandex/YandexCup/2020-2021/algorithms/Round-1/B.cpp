/**
 *	Author:		antikostya
 *	Created:	2021-10-03 20:35:12
 *	Modified:	2021-10-03 20:53:05
 **/

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace::std;

class Tile
{
public:
	string	a;

	Tile(const string &st1, const string &st2)
	{
		string st = st2;
		reverse(st.begin(), st.end());
		a = st1 + st;
	}

	Tile(const string &st)
	{
		a = st;
	}

	Tile rotate(void)
	{
		return (Tile(a.substr(1) + a[0]));
	}

	bool operator ==(const Tile &other)
	{
		return a == other.a;
	}
};

int	main()
{
	vector<Tile>			tiles;
	uint					n, m;

	cin >> n;
	tiles.resize(n);
	for (uint i=0; i < n; ++i)
	{
		string st1, st2;
		cin >> st1 >> st2;
		tiles[i] = Tile(st1, st2);
	}
	cin >> n >> m;
	for (uint y=0; y < n / 2; ++y)
	{
		string st1, st2;
		cin >> st1 >> st2;
		stringstream s1(st1);
		stringstream s2(st2);
		for (uint x=0; x < n / 2; ++x)
		{
			st1 = string(s1.get()) + s1.get();
			st2 = string(s2.get()) + s2.get();
			Tile carp(st1, st2);
			bool ok = false;
			for (const auto tile : tiles)
			{
				for (uint i=0; i < 4; ++i)
				{
					if (tile == carp)
						ok = true;
					break
				}
				if (ok)
					break;
			}
			if (not ok)
			{
				cout << "No" << endl;
				return (0);
			}
		}
	}
	cout << "Yes" << endl;
}

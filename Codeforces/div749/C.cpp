/**
 *	Author:		antikostya
 *	Created:	2021-10-17 15:37:59
 *	Modified:	2021-10-17 16:22:06
 **/

#include <bits/stdc++.h>

using namespace::std;

int main()
{
	int	X, Y;

	cin >> Y >> X;
	vector<string> MAP(Y);
	for (int i=0; i < Y; ++i)
	{
		cin >> MAP[i];
	}
	vector<vector<int>> gd(Y);
	for (int y=0; y < Y; ++y)
	{
		gd[y].resize(X, 0);
		gd[y][0] = 1;
		if (MAP[y][0] == 'X')
		{
			gd[y][0] = 0;
		}
	}
	for (int x=0; x < X; ++x)
	{
		gd[0][x] = 1;
		if (MAP[0][x] == 'X')
		{
			gd[0][x] = 0;
		}
	}
	for (int x=1; x < X; ++x)
	{
		for (int y=1; y < Y; ++y)
		{
			if (MAP[y][x] == 'X')
				continue;
			gd[y][x] = gd[y - 1][x] or gd[y][x - 1];
		}
	}
	vector<bool> col_def(X, 0);
	for (int x=0; x < X; ++x)
	{
		bool is_def = 1;
		for (int y=0; y < Y; ++y)
		{
			if ((gd[y][x] == 1 and MAP[y][x] == 'X') or
				(gd[y][x] == 0 and MAP[y][x] == '.'))
			{
				is_def = 0;
				break;
			}
		}
		col_def[x] = is_def;
	}
	vector<int> bad_array(X, 0);
	int last_bad = -1;
	for (int x=X - 1; x >= 0; --x)
	{
		if (col_def[x])
		{
			last_bad = x;
			break;
		}
	}
	for (int i=X - 1; i >=0; --i)
	{
		if (col_def[i])
		{
			last_bad = i;
		}
		bad_array[i] = last_bad;
	}
	int n;
	cin >> n;
	while (n--)
	{
		int l, r;
		cin >> l >> r;
		--l;
		--r;
		if (bad_array[l] < r)
		{
			cout << "NO" << endl;
		}
		else
		{
			cout << "YES" << endl;
		}
	}
}

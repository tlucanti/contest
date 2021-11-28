/*
* @Author: kostya
* @Date:   2021-11-14 15:55:42
* @Last Modified by:   kostya
* @Last Modified time: 2021-11-14 16:17:02
*/

#include <iostream>
#include <vector>

using namespace::std;

class point
{
public:
	int x;
	int y;

	point(int _x, int _y)
		: x(_x), y(_y) {}

	point operator +(const point &other)
	{
		return point(x + other.x, y + other.y);
	}

	point &operator +=(const point &other)
	{
		x = other.x + x;
		y = other.y + y;
		return *this;
	}

	point &operator =(const point &other)
	{
		x = other.x;
		y = other.y;
		return *this;
	}

	bool operator ==(const point &other)
	{
		return x == other.x and y == other.y;
	}

	bool operator !=(const point &other)
	{
		return x != other.x or y != other.y;
	}
};

vector<point> DIRS = {
	point(0, 1), point(0, -1), point(1, 0), point(-1, 0)
};
vector<vector<int>> MAP(1001);

void dfs(point start, point direct)
{
	start = start + direct;
	while (
			start.x >= 0 and start.x <= 1000
		and start.y >= 0 and start.y <= 1000
		)
	{
		if (MAP[start.x][start.y] == 0)
		{
			MAP[start.x][start.y] = 1;
			for (point dir : DIRS)
			{
				if (dir != direct)
					dfs(start, dir);
			}
		}
		start += direct;
	}
}

int main()
{
	int n;
	cin >> n;
	vector<point> drifts;
	for (int i=0; i < 1001; ++i)
		MAP[i].resize(1001);
	for (int x=0; x < 1001; ++x)
		for (int y=0; y < 1001; ++y)
			MAP[x][y] = -1;
	for (int i=0; i < n; ++i)
	{
		int x, y;
		cin >> x >> y;
		point snow(x, y);
		drifts.push_back(snow);
		MAP[x][y] = 0;
	}
	int ans = 0;

	for (point snow : drifts)
	{
		if (MAP[snow.x][snow.y] == 0)
		{
			MAP[snow.x][snow.y] = 1;
			for (point dir : DIRS)
				dfs(snow, dir);
			++ans;
		}
	}
	cout << ans - 1 << endl;
}

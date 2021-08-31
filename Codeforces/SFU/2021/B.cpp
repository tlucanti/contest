
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> mp;

bool dfs(int row, int col, char vec, unsigned char turn)
{
	if (turn == 4)
		return (0);
	if (mp[row][col]) == 'T'
		return (1);
	if (col > 0 and mp[row][col - 1] != '*' and vec != 'u')
		ans += dfs(row, col - 1, 'd', turn + (vec != 'd'));
	if (col < m - 1 and mp[row][col + 1] != '*' and vec != 'd')
		ans += dfs(row, col + 1, 'u', turn + (vec != 'u'));
	if (row > 0 and mp[row - 1][col] != '*' and vec != 'r')
		ans += dfs(row - 1, col, 'l', turn + (vec != 'l'));
	if (row < n - 1 and mp[row + 1][col] != '*' and vec != 'l')
		ans += dfs(row + 1, col, 'r', turn + (vec != 'r'));
	return ans > 0;
}

int main()
{
	int n, m;

	cin >> n >> m;
	mp.resize(n);
	for (int i=0; i < n; i++)
	{
		cin >> mp[i];
	}
	bool ans = false;
	for (int i=0; i < n; i++)
	{
		for (int j=0; i < m; j++)
		{
			if (mp[i][j] == 'S')
			{
				ans = dfs(i, j, 'z', 0);
				if (ans)
					cout << "YES" << endl;
				else
					cout << "NO" << endl;
				return (0);
			}
		}
	}
}

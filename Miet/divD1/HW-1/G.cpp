/*
* @Author: kostya
* @Date:   2021-11-13 16:57:33
* @Last Modified by:   kostya
* @Last Modified time: 2021-11-13 17:02:25
*/

#include <string>
#include <iostream>

using namespace::std;

int main()
{
	int n, t;
	string s;
	cin >> n >> t >> s;
	while (t--)
	{
		for (int i=1; i < n; ++i)
			if (s[i] == 'G')
				swap(s[i], s[i - 1]);
	}
	cout << s << endl;
}

BGGBG
GBGGB
